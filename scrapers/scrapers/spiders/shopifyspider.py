from scrapy.spiders import FilteredSitemapSpider


class ShopifyCrawler(FilteredSitemapSpider):
    name = 'shopify'
    allowed_domains = [
        'https://apps.shopify.com'
    ]

    sitemap_urls = [
        'https://apps.shopify.com/sitemap.xml',
    ]

    sitemap_rules = [
        ('https://apps.shopify.com', 'parse_item'),
    ]

    def parse_item(self, response):
        yield {
            "name": response.css("h1::text").get().strip(),
            "url": "",
            # response.css("div.ui-app-pricing::text").get().replace("Price: ", "").strip(),
            "packages": [],
            "ratings": response.css("span.tw-text-body-sm.tw-text-fg-secondary::text").get().replace("Rating (", "").replace(")", "").strip(),
            "reviews": response.css("#reviews-link.tw-group.tw-text-link-md::text").get().strip().replace(",", ""),
            "developer": response.css(".tw-text-body-md .tw-group::text").get().strip(),
            "description": "",
            "launched": response.css("p:nth-child(2).tw-text-fg-tertiary.tw-text-body-sm::text").get().strip(),
            "languages":  response.css("h1::text").get().strip(),
            "categories":  response.css("h1::text").get().strip(),
            "works_with":  "",
        }


skip_urls = ['https://apps.shopify.com/categories/',
             'https://apps.shopify.com/app-groups/',
             'https://apps.shopify.com/stories/',
             'https://apps.shopify.com/collections/',
             'https://apps.shopify.com/partners/'
             ]


def sitemap_filter(self, entries):
    for entry in entries:
        if entry.get('loc') not in skip_urls:
            yield entry
