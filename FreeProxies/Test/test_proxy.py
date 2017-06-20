import requests
r = requests.get('http://www.baidu.com', proxies={'https':'http://61.159.138.62:808'}, timeout=60)
print(r.request.prepare_body)
