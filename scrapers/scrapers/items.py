# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapersItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    packages = scrapy.Field()
    ratings = scrapy.Field()
    reviews = scrapy.Field()
    developer = scrapy.Field()
    description = scrapy.Field()
    launched = scrapy.Field()
    categories = scrapy.Field()
    works_with = scrapy.Field()


class Price(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()


class Developer(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
