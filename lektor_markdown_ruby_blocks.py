import re
from collections import namedtuple

from lektor.pluginsystem import Plugin

# group 1: color of the text, group 2: the content
rb_block_pattern = re.compile(r'^\^\^(#[0-9a-fA-F]{6,8})?\n(.*)\^\^$', flags=re.DOTALL)
# group 1: base text, group 2: ruby text
ruby_pattern = re.compile(r'\((.+?)\)\[(.+?)]')


def convert(base, ruby):
    return f'<ruby>{base}<rp>(</rp><rt>{ruby}</rt><rp>)</rp></ruby>'


Conversion = namedtuple('Conversion', 'span text')


class RubyBlockMixin:
    def paragraph(self, text):
        match = rb_block_pattern.match(text)
        if match is None:
            return super().paragraph(text)
        color = match[1]
        ruby_text = self._rubify(match[2].strip(), color)

        return f'<p>{ruby_text}</p>'

    def _rubify(self, content, color):
        lines = content.split('\n')
        converted_line = []
        for line in lines:
            if line.startswith('% '):
                rb_line = self._rubify_line(line[2:], None, ignore=True)
            else:
                rb_line = self._rubify_line(line, color)
            converted_line.append(rb_line)
        return '<br />\n'.join(converted_line)

    def _rubify_line(self, line, color, ignore=False):
        if line == "-##-":
            return ''
        elif ignore:
            return f'<span class="non-ruby-line">{line}</span>'

        cvts = self._collect_convertions(line)
        for (start, end), rt in cvts[::-1]:
            line = line[:start] + rt + line[end:]

        if color is not None:
            rb_line = f'<span class="ruby-line" style="color: {color};">{line}</span>'
        else:
            rb_line = f'<span class="ruby-line">{line}</span>'

        return rb_line

    def _collect_convertions(self, line):
        replacement = []
        for match in ruby_pattern.finditer(line):
            base, ruby = match[1].split('|'), match[2].split('|')
            cvt_text = ''.join(convert(b, r) for b, r in zip(base, ruby))
            replacement.append(Conversion(match.span(), cvt_text))
        return replacement


class RubyBlockPlugin(Plugin):
    name = 'Markdown Ruby Block'
    description = 'Add supports to ruby blocks syntax in Markdown'

    def on_markdown_config(self, config, **extra):
        config.renderer_mixins.append(RubyBlockMixin)
