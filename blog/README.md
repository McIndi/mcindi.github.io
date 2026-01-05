# Blog Post Wrapper System

This directory contains a template and script system for wrapping blog post content with the McIndi Solutions website design.

## Files

- **blog-post-template.html** - The HTML template with placeholders
- **wrap_blog_post.py** - Python script to wrap content with the template
- **example-config.json** - Example configuration file

## Quick Start

### Method 1: Using a Config File (Recommended)

1. Create your blog post content (just the body HTML, no wrapper)
2. Create a config JSON file with your post metadata
3. Run the wrapper script:

```bash
python wrap_blog_post.py my-content.html output.html --config my-config.json
```

### Method 2: Using Command Line Arguments

```bash
python wrap_blog_post.py my-content.html output.html \
  --title "My Blog Post Title" \
  --slug "my-blog-post" \
  --date "January 5, 2026" \
  --category "Enterprise Architecture" \
  --author "Cliff"
```

## Configuration File Format

Create a JSON file with the following fields:

```json
{
  "title": "Your Blog Post Title",
  "slug": "url-friendly-slug",
  "meta_description": "SEO description for search engines",
  "category": "Category or Eyebrow Text",
  "subtitle": "Optional subtitle text",
  "publish_date": "Month DD, YYYY",
  "author": "Author Name",
  "cta_title": "Call-to-Action Title",
  "cta_description": "CTA description text",
  "cta_email_subject": "Email%20Subject%20URL%20Encoded"
}
```

### Required Fields

- `title` - The main blog post title
- `slug` - URL-friendly version (e.g., "my-blog-post")
- `publish_date` - Publication date

### Optional Fields (have defaults)

- `meta_description` - Defaults to generic company description
- `category` - Defaults to "Enterprise Architecture & Technology Leadership"
- `subtitle` - Defaults to empty (no subtitle)
- `author` - Defaults to "McIndi Solutions"
- `cta_title` - Defaults to generic CTA
- `cta_description` - Defaults to generic company pitch
- `cta_email_subject` - Defaults to "Technology%20Strategy%20Discussion"

## Content Format

Your content file should contain just the article body HTML - no DOCTYPE, html, head, or body tags. The script will wrap it with the full page structure.

Example content structure:

```html
<h2>Introduction</h2>
<p>Your content here...</p>

<h3>Subsection</h3>
<p>More content...</p>

<pre><code>Code blocks work too</code></pre>
```

## Template Placeholders

The template uses these placeholders (automatically replaced by the script):

- `{{BLOG_TITLE}}` - Blog post title
- `{{BLOG_SLUG}}` - URL slug
- `{{META_DESCRIPTION}}` - Meta description
- `{{CATEGORY}}` - Category/eyebrow text
- `{{SUBTITLE}}` - Optional subtitle (wrapped in `<p class="subtitle">`)
- `{{PUBLISH_DATE}}` - Publication date
- `{{AUTHOR}}` - Author name
- `{{CONTENT}}` - Your blog post content
- `{{CTA_TITLE}}` - CTA section title
- `{{CTA_DESCRIPTION}}` - CTA description
- `{{CTA_EMAIL_SUBJECT}}` - Email subject (URL encoded)

## Examples

### Example 1: Django Tutorial Post

```bash
python wrap_blog_post.py django-content.html django-saas-mega-tut-001.html \
  --config example-config.json
```

### Example 2: Quick Post with Minimal Config

```bash
python wrap_blog_post.py quick-tip.html quick-tip-output.html \
  --title "Quick DevOps Tip" \
  --slug "quick-devops-tip" \
  --date "January 5, 2026"
```

This will use all default values for optional fields.

## Adding to Blog Index

After creating your blog post, add it to [index.html](./index.html) by copying the blog entry template:

```html
<article class="card">
  <span class="badge">Category</span>
  <h3><a href="./your-post.html">Your Post Title</a></h3>
  <p class="blog-meta">Published on <time datetime="YYYY-MM-DD">Month DD, YYYY</time></p>
  <p>Brief excerpt or summary...</p>
  <a href="./your-post.html" class="btn btn-ghost">Read More</a>
</article>
```

## CSS Styling

All blog post styling is defined in [../styles.css](../styles.css) under the "Blog Styles" and "Blog Article Content" sections. The styling supports:

- Headings (h2, h3)
- Paragraphs with proper line height
- Lists (ul, ol)
- Code blocks (pre/code)
- Inline code
- Links
- Blockquotes
- Horizontal rules
- Strong/em text
- Mobile responsiveness

## Tips

1. **URL Encoding**: For email subjects, use URL encoding (spaces become `%20`)
2. **Subtitle**: Leave empty if you don't need one
3. **Consistency**: Use consistent category names across posts
4. **SEO**: Write descriptive meta descriptions (150-160 characters)
5. **Slug**: Keep slugs short, lowercase, with hyphens
