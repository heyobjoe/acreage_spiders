# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose

# def convert_title(title):
#     if title:
#         return title.strip()


def convert_price(price):
    if price:
        return price #filter(str.isdigit, price)

def convert_link(link):
    if "http" not in link:
        return 'https://www.arrowalternativecare.com' + link
    else:
        return link





class ProductItem(scrapy.Item):
    title = scrapy.Field()
    size = scrapy.Field()
    price = scrapy.Field(
        input_processor = MapCompose(convert_price)
    )
    link = scrapy.Field(
        input_processor = MapCompose(convert_link)
    )
