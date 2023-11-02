from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader


def remove_comma(value):
    return value.replace(",", "").strip()


def clean_ratings(value):
    return value.replace("Rating (", "").replace(")", "").strip()

def process_developer(value):
    # Process the list of dictionaries and extract 'name' and 'url'
    formatted_developers = [f"{entry['name']} ({entry['url']})" for entry in value]
    return formatted_developers


class ShopifyLoader(ItemLoader):
    default_output_processor = TakeFirst()

    categories_in = MapCompose(str.strip)
    description_in = MapCompose(str.strip)
    # developer_in = MapCompose(str.strip)
    languages_in = MapCompose(str.strip)
    launched_in = MapCompose(str.strip)
    logo_in = MapCompose(str.strip)
    name_in = MapCompose(str.strip)
    # packages_in = MapCompose(str.strip)
    # ratings_in = MapCompose(clean_ratings)
    reviews_in = MapCompose(remove_comma)
    url_in = MapCompose(str.strip)
    works_with_in = MapCompose(str.strip)
