'''
Crawl the site to get OID data
'''

import requests
url = 'https://www.der-windows-papst.de/2020/10/18/certificate-oids-and-key-usage-extensions/'
headers = {
    'UA-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

rep = requests.get(url=url,headers=headers)
page_text = rep.text
filename = 'oid' + '.txt'
with open(filename,'w',encoding='utf=8') as fp:
    fp.write(page_text)
