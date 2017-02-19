import re
from urlparse import urljoin
from urlparse import urlparse
from bs4 import BeautifulSoup
import urllib2
from time import sleep

url=raw_input('URL= ')

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open(url)
content = response.read()


pattern=re.compile(r'https://www.amazon.in/.*/dp/(.*?)/')
asin=set(re.findall(pattern,content))
print(asin)
asin=list(asin)
links=[]
for pid in asin:
    link=urljoin("https://www.amazon.in/dp/",pid)
    links.append(link)
    print("processing : "+str(link))
    response = opener.open(link)
    html = response.read()
    page = BeautifulSoup(html)
    TITLE =str(page.find(id="productTitle").getText())
    PRICE = re.findall(r'<span id="priceblock_ourprice" class="a-size-medium a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>(.+?)</span>'or r'''span class='a-color-price'><span class="currencyINR">&nbsp;&nbsp;</span> (.+?)</span></span>''',html)
    AVAILABILITY = re.findall(r'[A-Z][a-z] stock'or r'[A-Z][a-z][a-z]',html)
    INFO=str(page.find("div",id="featurebullets_feature_div").find("div").findAll("span")[2].getText())
    URL=url
 
        

    data = {
            'TITLE':TITLE,
            'PRICE':PRICE,
            'AVAILABILITY':AVAILABILITY,
            'INFO':INFO,
            'URL':URL,
            }
    print(data)
    sleep(3)


