# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst

def clean_item(value):
    # Remove leading and trailing spaces and newline characters, as well as spaces within the text
    return value.strip().replace('\n', '').replace(' ', '')

def to_array(value):
    value = value.strip("'")  # Remove single quotes around the string
    return [lang.strip().replace('and ', '') for lang in value.split(', ')]

def to_float(value):
    try:
        rating = float(value.split('(')[-1].split(')')[0])
        return rating
    except (ValueError, IndexError):
        return None
    
def to_int(value):
    value = value.strip().replace('\n', '').replace(' ', '')
    try:
        if 'K' in value:
            numeric_part = float(value.replace('K', '').strip())
            return int(numeric_part * 1000)
        elif 'M' in value:
            numeric_part = float(value.replace('M', '').strip())
            return int(numeric_part * 1000000)
        else:
            return int(value)
    except (ValueError, TypeError):
        return None  

class ScrapersItem(scrapy.Item):
    active_installations = scrapy.Field()
    categories = scrapy.Field(
        output_processor=MapCompose(to_array)
    )
    description = scrapy.Field()
    developer = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    languages = scrapy.Field(
        output_processor=MapCompose(to_array)
    )
    last_updated = scrapy.Field()
    launched = scrapy.Field()
    logo = scrapy.Field()
    name = scrapy.Field()
    packages = scrapy.Field()
    php_version = scrapy.Field()
    ratings = scrapy.Field()
    reviews = scrapy.Field(
        input_processor=MapCompose(to_int)
    )
    support = scrapy.Field()
    tags = scrapy.Field()
    tested_up_to = scrapy.Field()
    url = scrapy.Field()
    version = scrapy.Field()
    wordpress_version = scrapy.Field()
    works_with = scrapy.Field(
        output_processor=MapCompose(to_array)
    )


class Package(scrapy.Item):
    description = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field(
        input_processor=MapCompose(clean_item),
        output_processor=TakeFirst()
    )


class Developer(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()


# Shopify gives the rating (average)
# Wordpress gives 1-5 stars, in these cases we need to calculate the average
class Rating(scrapy.Item):
    average = scrapy.Field(
        input_processor=MapCompose(to_float)
    )
    five_star = scrapy.Field(
        input_processor=MapCompose(to_int)
    )
    four_star = scrapy.Field(
        input_processor=MapCompose(to_int)
    )
    one_star = scrapy.Field(
        input_processor=MapCompose(to_int)
    )
    three_star = scrapy.Field(
        input_processor=MapCompose(to_int)
    )
    two_star = scrapy.Field(
        input_processor=MapCompose(to_int)
    )
