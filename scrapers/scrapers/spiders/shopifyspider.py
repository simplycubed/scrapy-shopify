from scrapy.spiders import SitemapSpider

from scrapers.items import ScrapersItem
from scrapers.itemsloaders import ShopifyLoader

# ONLY for Testing
allow_urls = [
    "https://apps.shopify.com/inbox"
]

skip_urls = [
    "https://apps.shopify.com/app-groups/",
    "https://apps.shopify.com/categories/",
    "https://apps.shopify.com/collections/",
    "https://apps.shopify.com/partners/",
    "https://apps.shopify.com/stories/",
]


class ShopifyCrawler(SitemapSpider):
    name = 'shopify'
    allowed_domains = [
        'apps.shopify.com'
    ]

    sitemap_urls = [
        'https://apps.shopify.com/sitemap.xml',
    ]

    sitemap_rules = [
        ('https://apps.shopify.com', 'parse_item'),
    ]

    def sitemap_filter(self, entries):
        for entry in entries:
            for substr in allow_urls:
                if substr in entry["loc"]:
                    yield entry

    def parse_item(self, response):
        l = ShopifyLoader(item=ScrapersItem(), response=response)
        l.add_css(
            "categories", "h1::text" # TEMP
        l.add_css("description", "h1::text")  # TEMP
        l.add_css("developer", ".tw-text-body-md .tw-group::text")
        l.add_xpath(
            "languages", "/html/body/main/section[4]/div/div/div[1]/div[2]/div/div[2]/p[2]/text()")
        l.add_css(
            "launched", "p:nth-child(2).tw-text-fg-tertiary.tw-text-body-sm::text")
        l.add_css("logo", "h1::text")  # TEMP
        l.add_css("name", "h1::text")
        l.add_css("packages", "h1::text")  # TEMP
        l.add_css("ratings", "span.tw-text-body-sm.tw-text-fg-secondary::text")
        l.add_css("reviews", "#reviews-link.tw-group.tw-text-link-md::text")
        l.add_css("url", "h1::text")  # TEMP
        l.add_css("works_with", "h1::text")  # TEMP
        return l.load_item()
