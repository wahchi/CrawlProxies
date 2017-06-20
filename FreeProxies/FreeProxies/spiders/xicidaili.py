# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from ..items import XiciProxies
class XicidailiSpider(scrapy.Spider):
    name = "xicidaili"
    allowed_domains = ["xicidaili.com"]
    start_urls = ['http://www.xicidaili.com/nn/']

    def parse(self, response):
        item = XiciProxies()
        proxy_divs = response.css('.odd')
        for proxy_div in proxy_divs:
            item['from_domain'] = self.name
            item['from_url'] = response.url
            item['ip_address'] = proxy_div.css('td::text')[0].extract()
            item['port'] = proxy_div.css('td::text')[1].extract()
            item['server_address'] = next(iter(proxy_div.css('a::text').extract()), "")
            item['is_anonymous'] = proxy_div.css('td::text')[4].extract()
            item['type'] = proxy_div.css('td::text')[5].extract()
            yield item





