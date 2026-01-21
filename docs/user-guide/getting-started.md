---
title: How to Automatically Submit Sitemap and URLs
description: Improve your SEO and learn how to automatically submit your website's sitemap and URLs to IndexNow for faster indexing by Bing, Yandex, DuckDuckGo, and other search engines. Includes code examples for beginners and advanced users.
tags:
    - SEO
    - IndexNow
    - Automation
    - GitHub Actions
    - Tutorial
    - Submit Sitemap
    - Submit URL
---

# User Guide to Workflow Automation 👨‍🔧
If you already use [GitHub Actions](https://github.com/features/actions) to automate workflows in your website projects, you can also use it to automate the process of submitting your sitemap to the IndexNow API.

This is particularly useful if you have a large number of pages on your site that you want to submit all at once so search engines know when to crawl your site for faster indexing by Bing, Yandex, DuckDuckGo and other search engines.

## How to Automatically Submit a Sitemap to IndexNow
Regardless of whether your codebase is highly or less active, it is recommended that you do _not_ submit your sitemap to IndexNow each time your site is deployed to production. This could overwhelm IndexNow and reduce the website's ranking.

Instead, you should automate sitemap submissions to IndexNow using GitHub Actions at regular intervals, allowing the changes to accumulate over time and allowing the search engines crawlers time to index the latest content.

Example workflow with GitHub Actions:

```yaml linenums="1" title=".github/workflows/submit_sitemap_to_index_now.yml"
name: Submit Sitemap to IndexNow

on:
  schedule:
    - cron: 0 0 1 * *  # Run at midnight UTC on the 1st day of each month.

jobs:
  submit-sitemap:
    runs-on: ubuntu-latest
    steps:
      - name: Submit sitemap URLs to IndexNow
        uses: jakob-bagterp/index-now-submit-sitemap-urls-action@v1
        with:
          host: example.com
          api_key: ${{ secrets.INDEX_NOW_API_KEY }}
          api_key_location: https://example.com/${{ secrets.INDEX_NOW_API_KEY }}.txt
          endpoint: yandex
          sitemap_locations: https://example.com/sitemap.xml
```

Want to know more about the parameters? Learn how to [customise your workflow parameters](parameters.md).

!!! abstract "Checklist"
    Before running the workflow, make sure you have done the following:

    - Added the API key `INDEX_NOW_API_KEY` as a [secret to your repository](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).
    - Uploaded the API key to the location specified in the `api_key_location` parameter.
    - Updated the URL of the sitemap in the `sitemap_location` parameter.
    - Adjusted the `host`, `endpoint`, and other parameters to suit your needs.

## Nested Sitemaps
If you have a sitemap index that links to other sitemaps, you only need to submit that in the `sitemap_locations` parameter. Both the index and the nested sitemaps will be included in the submission to the IndexNow API.

### Example
If you have a sitemap index that links to two other sitemaps, for example, URLs from all three sitemaps will be included in the submission to the IndexNow API.

```xml linenums="1" title="sitemap_index.xml" hl_lines="4 7"
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <sitemap>
        <loc>https://example.com/sitemap1.xml</loc>
    </sitemap>
    <sitemap>
        <loc>https://example.com/sitemap2.xml</loc>
    </sitemap>
</urlset>
```

In this case, you only need to submit a single sitemap with a link to `sitemap_index.xml` as the location.

!!! info
    Only sitemaps on levels 1 and 2 are supported. Nested sitemaps on level 3 and beyond will be ignored.
