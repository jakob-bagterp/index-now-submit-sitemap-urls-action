from datetime import datetime, timedelta

from index_now.sitemap.parse import SitemapUrl

SITEMAP_URLS = [
    SitemapUrl(loc="https://example.com/section1/page1", lastmod=str(datetime.today().date())),
    SitemapUrl(loc="https://example.com/section2/page1", lastmod=str((datetime.today() - timedelta(days=1)).date())),
    SitemapUrl(loc="https://example.com/section2/page2", lastmod=str((datetime.today() - timedelta(days=2)).date())),
]

URLS = [url.loc for url in SITEMAP_URLS]
