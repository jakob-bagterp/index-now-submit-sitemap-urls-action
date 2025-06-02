---
title: Customise Your Workflow Parameters
description: Improve your SEO and learn how to automatically submit your website's sitemap and URLs to IndexNow for faster indexing by Bing, Yandex, DuckDuckGo, and other search engines. Includes code examples for beginners and advanced users.
tags:
    - SEO
    - IndexNow
    - Automation
    - GitHub Actions
    - API Key
    - Tutorial
    - API Endpoint
    - Bing
    - Naver
    - Seznam
    - Yandex
    - Yep
---

# How to Customise Your Workflow Parameters
Using the flexible parameters, you can submit individual or multiple URLs, or even entire or partial sitemaps, to IndexNow on a regular basis. Find out how based on the following example:

```yaml linenums="1" title=".github/workflows/submit_sitemap_to_index_now.yml"
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
          host: example.com
          api_key: ${{ secrets.INDEX_NOW_API_KEY }}
          api_key_location: https://example.com/${{ secrets.INDEX_NOW_API_KEY }}.txt
          endpoint: yandex
          urls: https://example.com
          sitemap_locations: https://example.com/sitemap.xml
          sitemap_filter: section1
          sitemap_days_ago: 2
```

## Overview
| Parameter           | Required | Description                                                                                                              | Default |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------ | ------- |
| `host`              | Yes      | The host of your website, e.g. `example.com`.                                                                            | `None`  |
| `api_key`           | Yes      | The API key for IndexNow, e.g. `a1b2c3d4`.                                                                               | `None`  |
| `api_key_location`  | Yes      | The location of the API key, e.g. `https://example.com/a1b2c3d4.txt`.                                                    | `None`  |
| `endpoint`          | Optional | The search engine endpoint, e.g. `indexnow`, `bing`, `naver`, `seznam`, `yandex`, `yep`.                                 | `bing`  |
| `urls`              | Optional | The URL(s) to be submitted, e.g. `https://example.com`.                                                                  | `None`  |
| `sitemap_locations` | Optional | The location of the sitemap(s), e.g. `https://example.com/sitemap.xml`.                                                  | `None`  |
| `sitemap_filter`    | Optional | Only submit sitemap URLs that contain the filter string, e.g. `section1`.                                                | `None`  |
| `sitemap_days_ago`  | Optional | Only submit sitemap URLs that have been modified recently based on the `<lastmod>` tag, e.g. `1`, `2`, or more days ago. | `None`  |

## Parameters
### `host`
Contains the domain (and subdomain) of your website. Required every time you submit any URLs or sitemaps to the IndexNow API.

For example, if the URL to your sitemap is `https://example.com`, then the `host` parameter should be `example.com`:

```yaml linenums="14" title=".github/workflows/submit_sitemap_to_index_now.yml"
          host: example.com
```

Or if your website URL is `https://www.example.com`, then the `host` should be `www.example.com`:

```yaml linenums="14" title=".github/workflows/submit_sitemap_to_index_now.yml"
          host: www.example.com
```

### `api_key`
The API key for IndexNow, e.g. `a1b2c3d4`. Required every time you submit any URLs or sitemaps to the IndexNow API.

You need to set an API key on your website to verify ownership of your domain. This should be kept secret and is required every time you submit a URL to the IndexNow API:

```yaml linenums="15" title=".github/workflows/submit_sitemap_to_index_now.yml"
          api_key: ${{ secrets.INDEX_NOW_API_KEY }}
```

If you don't want to use the [API key generator from Microsoft Bing](https://www.bing.com/indexnow/getstarted#implementation), you can [create your own API key](https://jakob-bagterp.github.io/index-now-for-python/user-guide/tips-and-tricks/generate-api-keys/#why-use-an-api-key).

!!! abstract "How to Keep Your API Key Secure"
    IndexNow requires an API key stored on your website, but how do you keep it secret and secure?

    For public repositories, you normally can't hide your IndexNow API key and its location – the file is visible in the repository code and the API key is exposed. It's therefore recommended to store your API key as a [secret in your repository](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).

### `api_key_location`
The location of the API key, e.g. `https://example.com/a1b2c3d4.txt`. Required every time you submit any URLs or sitemaps to the IndexNow API.

Similar to the `api_key`, the location of your API key should be kept secret:

```yaml linenums="16" title=".github/workflows/submit_sitemap_to_index_now.yml"
          api_key_location: https://example.com/${{ secrets.INDEX_NOW_API_KEY }}.txt
```

### `endpoint`
Optional. The search engine endpoint, e.g. `indexnow`, `bing`, `naver`, `seznam`, `yandex`, `yep`. If not specified, Bing is used as the default endpoint.

```yaml linenums="17" title=".github/workflows/submit_sitemap_to_index_now.yml"
          endpoint: yandex
```

!!! warning
    It is not recommended to submit the same URLs to multiple endpoints. Once you have successfully submitted to one [IndexNow](https://www.indexnow.org) endpoint, the IndexNow service is designed to propagate your URLs to other search engines, so you do not need to submit to multiple times.

### `urls`
Optional. The URL(s) to be submitted to IndexNow. Can be an individual URL, e.g. `https://example.com`:

```yaml linenums="18" title=".github/workflows/submit_sitemap_to_index_now.yml"
          urls: https://example.com
```

Or multiple URLs as comma separated list:

```yaml linenums="18" title=".github/workflows/submit_sitemap_to_index_now.yml"
          urls: https://example.com/page1, https://example.com/page2
```

### `sitemap_locations`
Optional. The location of the sitemap(s) from which the URLs will be submitted to IndexNow. Can be an individual sitemap, e.g. `https://example.com/sitemap.xml`:

```yaml linenums="19" title=".github/workflows/submit_sitemap_to_index_now.yml"
          sitemap_locations: https://example.com/sitemap.xml
```

Or multiple sitemaps as comma separated list:

```yaml linenums="19" title=".github/workflows/submit_sitemap_to_index_now.yml"
          sitemap_locations: https://example.com/sitemap1.xml, https://example.com/sitemap2.xml
```

### `sitemap_filter`
Optional. Only submit sitemap URLs that contain the filter string, e.g. `section1`. Optional.

```yaml linenums="20" title=".github/workflows/submit_sitemap_to_index_now.yml"
          sitemap_filter: section1
```

Or filter the sitemap URLs for both `section1` and `section2` using a regular expression:

```yaml linenums="20" title=".github/workflows/submit_sitemap_to_index_now.yml"
          sitemap_filter: "r'(section1)|(section2)'"
```

### `sitemap_days_ago`
Optional. Only submit sitemap URLs that have been modified recently based on the `<lastmod>` tag, e.g. `1`, `2`, or more days ago.

For example, all sitemap URLs that have been modified in the last week days will be submitted:

```yaml linenums="21" title=".github/workflows/submit_sitemap_to_index_now.yml"
          sitemap_days_ago: 7
```

Or only submit sitemap URLs that have been modified since yesterday:

```yaml linenums="21" title=".github/workflows/submit_sitemap_to_index_now.yml"
          sitemap_days_ago: 1
```

Or only submit sitemap URLs that have been modified today:

```yaml linenums="21" title=".github/workflows/submit_sitemap_to_index_now.yml"
          sitemap_days_ago: 0
```
