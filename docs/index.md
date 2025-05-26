---
title: Automatically Submit Sitemap and URLs to IndexNow 🔎
description: This workflow with GitHub Actions will automatically submit your website's sitemap and URLs to IndexNow for faster indexing by Bing, Yandex, DuckDuckGo, and other search engines.
tags:
    - SEO
    - IndexNow
    - Automation
---

[![Latest version](https://img.shields.io/static/v1?label=version&message=1.0.9&color=yellowgreen)](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/releases/latest)
[![MIT license](https://img.shields.io/static/v1?label=license&message=MIT&color=blue)](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/index-now-submit-sitemap-urls-action/branch/master/graph/badge.svg?token=PEGUV7IL8T)](https://codecov.io/gh/jakob-bagterp/index-now-submit-sitemap-urls-action)
[![CodeQL](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/actions/workflows/codeql.yml/badge.svg)](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/actions/workflows/codeql.yml)
[![Test](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/index-now-submit-sitemap-urls-action/actions/workflows/test.yml)

# Automate Sitemap and URL Submission to IndexNow 🔎
## Why Use IndexNow?
Are you concerned about search engine optimisation (SEO)? And do you want to make sure that your website is frequently indexed by [Bing](https://www.bing.com/indexnow), [Yandex](https://yandex.com/indexnow), [DuckDuckGo](https://duckduckgo.com/) and other search engines that support [IndexNow](https://www.indexnow.org/)?

Imagine submitting all your sitemap URLs to IndexNow when your website is updated, so that search engines know when to crawl your site again. This is what this action does.

!!! note "What is IndexNow?"
    [IndexNow](https://www.indexnow.org/) is an open source protocol that allows website owners to notify search engines when their content has changed, so that search engines can quickly crawl and index the new content. This is particularly useful for sites that update frequently or have dynamic content, and it is useful for search engines to know which pages to crawl and index since the last visit.

    By using IndexNow, you can ensure that your website is indexed more frequently, which can improve your search engine rankings and drive more traffic to your site.

    Search engines such as [Bing](https://www.bing.com/indexnow), [Yandex](https://yandex.com/indexnow), [DuckDuckGo](https://duckduckgo.com/) (via Bing's index) and others already support IndexNow, but not all search engines. For example, Google is not on board, but this may change in the future.

## How to Automatically Submit Sitemap and URLs to IndexNow
This workflow for GitHub Actions will automatically submit your sitemap to IndexNow for faster indexing by Bing, Yandex, DuckDuckGo and other search engines.

If you're already using GitHub Actions, simply add this action to your workflow. It can automatically submit your sitemap to IndexNow whenever you deploy changes to your site.

!!! abstract "How to Keep Your API Key Secure"
    IndexNow requires an API key stored on your website, but how do you keep it secret and secure?

    For public repositories, you normally can't hide your IndexNow API key and its location – the file is visible in the repository code and the API key is exposed.

    However, with this action, the API key is generated on the fly and cached until the sitemap is successfully submitted and accepted by IndexNow. After that, the file will be removed from the repository.

## Next Steps
Ready to try? Find more information on [GitHub's Marketplace](https://github.com/marketplace/actions/index-now-submit-action).

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
