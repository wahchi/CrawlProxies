import scrapy
from twisted.internet import reactor

from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
from FreeProxies.spiders.xicidaili import XicidailiSpider
from apscheduler.schedulers.background import BackgroundScheduler
import time
from scrapy.utils.project import get_project_settings
import os
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
# def task():
#
# progress = CrawlerProcess(get_project_settings())
#
# progress.crawl(XicidailiSpider)
#
# progress.start(stop_after_crawl=False)    # Do not stop reactor after spider closes
#

#
# def run_crawl():
#     """
#     Run a spider within Twisted. Once it completes,
#     wait 5 seconds and run another spider.
#     """
#     runner = CrawlerRunner(get_project_settings())
#     deferred = runner.crawl(XicidailiSpider)
#
#     # you can use reactor.callLater or task.deferLater to schedule a function
#     deferred.addCallback(reactor.callLater, 10, run_crawl)
#     return deferred
#
# run_crawl()
# reactor.run()
while(True):
    runner = CrawlerRunner()

    d = runner.crawl(XicidailiSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run(True) # the script will block here until the crawling is finished
    time.sleep(15)