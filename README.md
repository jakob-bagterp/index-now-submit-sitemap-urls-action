[![Latest version](https://img.shields.io/static/v1?label=version&message=1.0.20&color=yellowgreen)](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/releases/latest)
[![MIT license](https://img.shields.io/static/v1?label=license&message=MIT&color=blue)](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/index-now-submit-sitemap-urls-action/branch/master/graph/badge.svg?token=PEGUV7IL8T)](https://codecov.io/gh/jakob-bagterp/index-now-submit-sitemap-urls-action)
[![CodeQL](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/actions/workflows/codeql.yml/badge.svg)](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/actions/workflows/codeql.yml)
[![Test](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/actions/workflows/test.yml)

# 🔍 Automatically Submit Sitemap URLs to IndexNow 🔎
Are you concerned about search engine optimization (SEO)? Do you want to make sure your website is indexed frequently by [Bing](https://www.bing.com/indexnow), [Yandex](https://yandex.com/indexnow), [DuckDuckGo](https://duckduckgo.com/), and other search engines?

This workflow for GitHub Actions will automatically submit your sitemap to IndexNow for faster indexing by Bing, Yandex, DuckDuckGo, and other search engines.

## How to Use
Example workflow:

```yaml
name: Submit Sitemap URLs to IndexNow

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
          host: example.com  # Replace with your website's host.
          api_key: ${{ secrets.INDEX_NOW_API_KEY }}  # Replace with your IndexNow API key.
          api_key_location: https://example.com/${{ secrets.INDEX_NOW_API_KEY }}.txt  # Replace with your IndexNow API key location.
          endpoint: yandex  # Optional. Other options: bing, indexnow, naver, seznam, yandex, yep. Default is Bing.
          sitemap_locations: https://example.com/sitemap.xml  # Replace with your sitemap location
          sitemap_filter: section1  # Optional. Only submit sitemap URLs that contain "section1" or match a regular expression "r'(section1)|(section2)'".
          sitemap_days_ago: 2  # Optional. Only submit sitemap URLs that have been modified recently, e.g. 1, 2, or more days ago.
```

> [!IMPORTANT]
> Before running the workflow, make sure you have done the following:
>
> * Added the API key `INDEX_NOW_API_KEY` as a [secret to your repository](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).
> * Uploaded the API key to the location specified in the `api_key_location` parameter.
> * Updated the URL of the sitemap in the `sitemap_location` parameter.
> * Adjusted the `host`, `endpoint`, and other parameters to suit your needs.

Ready to try? [Let's get started](https://jakob-bagterp.github.io/index-now-submit-sitemap-urls-action/).

## Become a Sponsor 🏅
If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution makes a difference, whether you buy a coffee or support with a monthly donation. Find your tier here:

[Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp)

Thank you for your support! 🙌

## Contribute
If you have suggestions or changes to the module, feel free to add to the code and create a [pull request](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/pulls).

## Report Bugs
If you encounter any issues, you can [report them as bugs or raise issues](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/issues).
