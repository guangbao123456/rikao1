# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    neirong = scrapy.Field()
    articleid = scrapy.Field()
    commentid = scrapy.Field()
    nickname = scrapy.Field()
    posttime = scrapy.Field()
    ip = scrapy.Field()

