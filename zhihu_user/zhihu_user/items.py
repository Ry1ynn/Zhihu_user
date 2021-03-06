# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuUserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    gender = scrapy.Field()
    headline = scrapy.Field()
    answer_count = scrapy.Field()
    url_token = scrapy.Field()
    articles_count = scrapy.Field()
    follower_count = scrapy.Field()
    description = scrapy.Field()

    # pass
