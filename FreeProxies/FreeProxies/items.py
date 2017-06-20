# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FreeproxiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class XiciProxies(scrapy.Item):
    from_domain = scrapy.Field()
    from_url = scrapy.Field()
    ip_address = scrapy.Field()
    port = scrapy.Field()
    server_address = scrapy.Field()
    is_anonymous = scrapy.Field()
    type = scrapy.Field()