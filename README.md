# lektor-markdown-ruby-blocks

This is a simple Lektor plugin that adds support for
HTML ruby tags to Markdown.

## Syntax 

To create a ruby tag, use the following **ruby-block** syntax:

```markdown
^^
(歩)[ある]く
^^
```

This will generate the following HTML:
```html
<span class="ruby-line">
  <ruby>歩<rp>(</rp><rt>ある</rt><rp>)</rp></ruby>く
</span>
```

The rendering result:

<span class="ruby-line">
  <ruby>歩<rp>(</rp><rt>ある</rt><rp>)</rp></ruby>く
</span>

You can combine adjacent ruby text like this:
```markdown
^^
(自|分)[じ|ぶん]
^^
```

And this will be rendered like this:
```html
<span class="ruby-line">
  <ruby>自<rp>(</rp><rt>じ</rt><rp>)</rp></ruby>
  <ruby>分<rp>(</rp><rt>ぶん</rt><rp>)</rp></ruby>
</span>
```

Rendered output:

<span class="ruby-line">
  <ruby>自<rp>(</rp><rt>じ</rt><rp>)</rp></ruby>
  <ruby>分<rp>(</rp><rt>ぶん</rt><rp>)</rp></ruby>
</span>

### Newline

This plugin will automatically add `<br />` between each line in a ruby-block:
```markdown
^^
(歩)[ある]く
(歩)[ある]く
^^
```
This will output:
```html
<span class="ruby-line">
  <ruby>歩<rp>(</rp><rt>ある</rt><rp>)</rp></ruby>く
</span>
<br />
<span class="ruby-line">
  <ruby>歩<rp>(</rp><rt>ある</rt><rp>)</rp></ruby>く
</span>
```

You can also use `-##-` to create an extra newline in a ruby-block. 
```markdown
^^
(歩)[ある]く
-##-
(歩)[ある]く
^^
```

Output:
```html
<span class="ruby-line">
  <ruby>歩<rp>(</rp><rt>ある</rt><rp>)</rp></ruby>く
</span>
<br />
<br />
<span class="ruby-line">
  <ruby>歩<rp>(</rp><rt>ある</rt><rp>)</rp></ruby>く
</span>
```

### Coloring the text

Additionally, you can add a 6-digit or 8-digit hex RGB code 
after the beginning `^^`, making the rendered content colored 
with specified color.

```markdown
^^#44cc00
(歩)[ある]く
^^
```

This will generate the following HTML pieces:
```html
<span class="ruby-line" style="color: #44cc00">
  <ruby>歩<rp>(</rp><rt>ある</rt><rp>)</rp></ruby>く
</span>
```

### Raw lines
Prepend `% ` &nbsp;to create a raw line. Raw lines are not converted to ruby tags, 
not affected by the color settings, and have a different class.

Example:
```markdown
^^#44cc00
(歩)[ある]く
% (aru)[ku]
^^
```

Output:
```html
<span class="ruby-line" style="color: #44cc00">
  <ruby>歩<rp>(</rp><rt>ある</rt><rp>)</rp></ruby>く
</span>
<br />
<span class="non-ruby-line">
  (aru)[ku]
</span>
```
