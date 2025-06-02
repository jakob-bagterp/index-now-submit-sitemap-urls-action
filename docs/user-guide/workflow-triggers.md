---
title: How to Trigger Worflows in GitHub Actions
description: If you're using GitHub Actions to deploy your website learn how to trigger workflows to automate the submission of your sitemap to the IndexNow API. Includes code examples for beginners and advanced users.
tags:
    - Automation
    - GitHub Actions
    - Tutorial
    - Workflow Dependency
    - Workflow Schedule
---

# How to Trigger Workflows in GitHub Actions
There are generally two ways to trigger workflows in GitHub Actions:

- **Time-based triggers**: For example, run a workflow on a weekly or daily schedule.
- **Event-based triggers**: For example, run a workflow new commit is pushed to the `master` branch or another workflow finishes.

## Scheduled and Time-Based Runs
The example below can be adjusted to run at different intervals. Simply adjust the [`cron` job](https://en.wikipedia.org/wiki/Cron) definition to your needs.

```yaml linenums="1" title=".github/workflows/submit_sitemap_to_index_now.yml"
name: Submit Sitemap URLs to IndexNow

on:
  schedule:
    - cron: 0 0 1 * *  # Run at midnight UTC on the 1st day of each month.
```

### Monthly Schedule
Run the workflow at midnight UTC on the first day of each month:

```yaml linenums="5" title=".github/workflows/submit_sitemap_to_index_now.yml"
    - cron: 0 0 1 * *
```

### Weekly Schedule
Run the workflow at midnight UTC on the first day of each week:

```yaml linenums="5" title=".github/workflows/submit_sitemap_to_index_now.yml"
    - cron: 0 0 * * 0
```

### Daily Schedule
Run the workflow at midnight UTC on a daily basis:

```yaml linenums="5" title=".github/workflows/submit_sitemap_to_index_now.yml"
    - cron: 0 0 * * *
```

!!! warning
    Too many submissions to any of the [IndexNow API endpoints](https://www.indexnow.org/searchengines.json) could result in your site being ranked lower by search engines, maybe even blacklisted. It's highly recommended to only submit sitemaps to the IndexNow API once a day or less, ideally only the latest updated URLs.

#### Only Submit Latest Changes
Rather than submitting all the URLs in the sitemap as one large payload to IndexNow, you can also submit only the latest changes by targeting the latest modification date of each URL in the sitemap using the `<lastmod>` tag. This is particularly useful if you have a large number of pages on your site that you want to submit all at once when deploying your site.

Simply adjust the [`sitemap_days_ago` parameter](parameters.md#sitemap_days_ago) to the desired number of days, as highlighted below:

```yaml linenums="1" title=".github/workflows/submit_sitemap_to_index_now.yml" hl_lines="19"
name: Submit Sitemap to IndexNow

on:
  schedule:
    - cron: 0 0 * * *  # Run daily at midnight UTC.

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
          sitemap_days_ago: 1
```

## Event-Triggered Workflows
Imagine the sitemap is submitted before the site has been fully deployed. This is something we want to avoid, as otherwise we won't be using the most up-to-date sitemap.

There are several ways to trigger workflows in GitHub Actions. The most common options in this context are:

- Use [`needs`](https://docs.github.com/en/actions/writing-workflows/about-workflows#creating-dependent-jobs) when having several jobs in the *same workflow file*.
- Use [`workflow_run`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_run) when you want to trigger jobs in *different workflow files*.

!!! tip
    If you want to update the previous workflow example, simple update the trigger to `workflow_run` instead of `schedule` and adapt the workflow names to your needs:

    ```yaml linenums="3" title=".github/workflows/submit_sitemap_to_index_now.yml"
    on:
      workflow_run:
        workflows: ["My Deployment Workflow"]
        branches: [master]
        types: [completed]
    ```

### GitHub Pages
For users of [GitHub Pages](https://pages.github.com), esepecally if you're using [MkDocs](https://www.mkdocs.org) or another tool to build your site with GitHub Pages, you can use this workflow to automatically submit the sitemap to IndexNow.

All you need to do is adjust the `on` condition and adapt the example below to your needs:


```yaml linenums="3" title=".github/workflows/submit_sitemap_to_index_now.yml"
on:
  workflow_run:
    workflows: [pages-build-deployment]
    types: [completed]
```

!!! info
    The [`workflow_run`](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#workflow_run) event is used to trigger the workflow after the GitHub Pages build and deployment is completed. This ensures that the sitemap is submitted only after the latest changes are live.
