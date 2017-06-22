import scrapy
from scrapy.crawler import CrawlerProcess
from FreeProxies.FreeProxies.spiders.xicidaili import XicidailiSpider
from apscheduler.schedulers.twisted import TwistedScheduler

progress = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})





sched = TwistedScheduler()
sched.add_job(progress.crawl, 'interval', args=[XicidailiSpider], seconds=10)
sched.start()
progress.start(False)    # Do not stop reactor after spider closes