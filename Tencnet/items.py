# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencnetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    job_name = scrapy.Field()
    # 详情链接
    detail_link = scrapy.Field()
    # 职位类别
    job_type = scrapy.Field()
    # 招聘人数
    number = scrapy.Field()
    # 工作地点
    address = scrapy.Field()
    # 发布时间
    pub_time = scrapy.Field()
    # 工作职责
    duty = scrapy.Field()
    # 招聘要求
    require = scrapy.Field()
