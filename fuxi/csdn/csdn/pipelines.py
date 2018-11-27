# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class CsdnPipeline(object):
    def __init__(self):
        myconn=MongoClient('127.0.0.1',27017)
        mydb=myconn['csdn']
        self.col=mydb['csdn20']
    def process_item(self, item, spider):
        self.col.insert(dict(item))
        return item
