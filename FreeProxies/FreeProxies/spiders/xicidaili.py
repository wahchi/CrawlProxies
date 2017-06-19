# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from ..items import XiciProxies
class XicidailiSpider(scrapy.Spider):
    name = "xicidaili"
    allowed_domains = ["xicidaili.com"]
    start_urls = ['http://xicidaili.com/nn']

    def parse(self, response):
        item = XiciProxies()
        proxy_divs = response.css('.odd')
        for proxy_div in proxy_divs:
            proxy_div.css('tr')
            pass
