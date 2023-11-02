from scrapy.spiders import SitemapSpider

from scrapers.items import ScrapersItem, Developer, Package, Rating
from scrapers.itemsloaders import ShopifyLoader

# Limiting to only 2 URLs for Testing
allow_urls = [
    "https://apps.shopify.com/inbox",
    "https://apps.shopify.com/tiktok"
]

# These URLs do not have apps, skipping
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

    # TEMP CSS selectors need to be updated and items loaders input processors updated
    def parse_item(self, response):
        l = ShopifyLoader(item=ScrapersItem(), response=response)
        d = ShopifyLoader(item=Developer(), response=response)
        p = ShopifyLoader(item=Package(), response=response)
        r = ShopifyLoader(item=Rating(), response=response)

        l.add_xpath("categories", 'normalize-space(//*[@id="adp-details-section"]/div/div/div[1]/div[2]/div/div[3]/span)') # TEMP
        l.add_xpath("description", 'normalize-space(//*[@id="app-details"])')  # TEMP

        # Update with items.Developer
        d.add_xpath("name", '//*[@id="adp-hero"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/a/text()')
        d.add_xpath("url", '//*[@id="adp-hero"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/a/@href')

        l.add_xpath(
            "languages", "/html/body/main/section[4]/div/div/div[1]/div[2]/div/div[2]/p[2]/text()")

        l.add_css(
            "launched", "p:nth-child(2).tw-text-fg-tertiary.tw-text-body-sm::text")
        l.add_css("logo", ".tw-rounded-sm.tw-block.tw-w-full::attr(src)")  # TEMP
        l.add_css("name", "h1::text")

        # Update with items.Package
        p.add_xpath("name", '//*[@id="adp-pricing"]/div[2]/div[1]/div/div/div/p[1]/text()')  # TEMP 
        p.add_xpath("price", '///*[@id="adp-pricing"]/div[2]/div[1]/div/div/div/h3/text()') 
        p.add_xpath("description", '//*[@id="adp-pricing"]/div[2]/div[1]/div/div/ul/text()')

        # Update with items.Rating
        r.add_css("average", "span.tw-text-body-sm.tw-text-fg-secondary::text")
        r.add_xpath("five_star", '//*[@id="adp-reviews"]/div/div/div[2]/div[1]/div[1]/div[3]/ul/li[1]/div[3]/a/span/text()')
        r.add_xpath("four_star", '//*[@id="adp-reviews"]/div/div/div[2]/div[1]/div[1]/div[3]/ul/li[2]/div[3]/a/span/text()')
        r.add_xpath("three_star", '//*[@id="adp-reviews"]/div/div/div[2]/div[1]/div[1]/div[3]/ul/li[3]/div[3]/a/span/text()')
        r.add_xpath("two_star", '//*[@id="adp-reviews"]/div/div/div[2]/div[1]/div[1]/div[3]/ul/li[4]/div[3]/a/span/text()')
        r.add_xpath("one_star", '//*[@id="adp-reviews"]/div/div/div[2]/div[1]/div[1]/div[3]/ul/li[5]/div[3]/a/span/text()')

        l.add_css("reviews", "#reviews-link.tw-group.tw-text-link-md::text")
        l.add_xpath("url", "/html/head/link[1]/@href")  # TEMP
        l.add_xpath("works_with", '/html/body/main/section[4]/div/div/div[1]/div[2]/div/div[4]/span/a/@href')  # TEMP
        l.add_xpath("support", '//*[@id="adp-developer"]/div/div/div/div[2]/p/text()')

        l.add_value("developer", d.load_item())
        l.add_value("packages", p.load_item())
        l.add_value("ratings", r.load_item())
        return l.load_item()
