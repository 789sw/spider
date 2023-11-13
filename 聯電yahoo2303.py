import requests
from bs4 import BeautifulSoup
url = "https://tw.stock.yahoo.com/quote/2303.TW" # 聯電
res = requests.get(url).text
soup = BeautifulSoup(res,'html5lib')
price_li = soup.find_all('li',{"class":"price-detail-item"})
title = []
content = []
for price in price_li :
    aaa = price.find_all('span')
    title.append(aaa[0].text.strip())
    content.append(aaa[1].text.strip())
for i in range(len(content)):
    print(title[i],content[i])