from crawlers.thanhnien import helper
from crawlers import common
import requests


def crawl():
    sitemap_url = 'https://thanhnien.vn/sitemaps/newsindex.xml'
    urls = common.extract_urls_from_sitemap(sitemap_url)
    for url in urls[:100]:
        print('URL: {}'.format(url))
        text = helper.extract_text_from_url(url)
        yield url, text
