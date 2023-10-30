# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapersItem(scrapy.Item):
    active_installations = scrapy.Field()
    categories = scrapy.Field()
    description = scrapy.Field()
    developer = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    languages = scrapy.Field()
    last_updated = scrapy.Field()
    launched = scrapy.Field()
    logo = scrapy.Field()
    name = scrapy.Field()
    packages = scrapy.Field()
    php_version = scrapy.Field()
    ratings = scrapy.Field()
    reviews = scrapy.Field()
    support = scrapy.Field()
    tags = scrapy.Field()
    tested_up_to = scrapy.Field()
    url = scrapy.Field()
    version = scrapy.Field()
    wordpress_version = scrapy.Field()
    works_with = scrapy.Field()


class Package(scrapy.Item):
    description = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()


class Developer(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()


# Shopify gives the rating (average)
# Wordpress gives 1-5 stars, in these cases we need to calculate the average
class Rating(scrapy.Item):
    average = scrapy.Field()
    five_star = scrapy.Field()
    four_star = scrapy.Field()
    one_star = scrapy.Field()
    three_star = scrapy.Field()
    two_star = scrapy.Field()
