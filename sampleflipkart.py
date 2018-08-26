import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/reebok-zeal-run-running-shoes-men/p/itmf6r3cmamgf5mu?pid=SHOF6R3FCH6JAFCX&lid=LSTSHOF6R3FCH6JAFCX3XWTPJ&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Deals%20of%20the%20Day_3_Min.40%25%2BExtra%2010%25%20Off_589975ZXLHGI_0&fm=organic&iid=77a19253-c1c1-4ad5-b641-3862f8658d6c.SHOF6R3FCH6JAFCX.SEARCH&ppt=StoreBrowse&ppn=Store'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,'html.parser')
name_box = soup.find('div', attrs={'class': '_1i0wk8'})
name = name_box.text.strip()
print (name)

name_box = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['qwjRop'])

for name in name_box:
	name = name.div.div
	content = name.text.strip()
	print(content)
