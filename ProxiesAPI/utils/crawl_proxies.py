import requests
from bs4 import BeautifulSoup
count = 0
# while(True):
#     html = requests.get('http://www.xicidaili.com/nn',
#                             headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"})

def crawl():
    html = requests.get('http://www.xicidaili.com/nn',
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"})
    bs_obj = BeautifulSoup(html.text, 'lxml')
    proxy_trs = bs_obj.find_all("tr", {"class": "odd"})
    for proxy_tr in proxy_trs:
        proxy = {}
        proxy['ip_address'] = proxy_tr.find_all('td')[1].get_text().strip()
        proxy['port'] = proxy_tr.find_all('td')[2].get_text().strip()
        proxy['server_address'] = proxy_tr.find_all('td')[3].get_text().strip()
        proxy['is_anonymous'] = proxy_tr.find_all('td')[4].get_text().strip()
        proxy['type'] = proxy_tr.find_all('td')[5].get_text().strip()
        yield proxy

print(crawl())