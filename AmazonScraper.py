from lxml import html  
import csv,os,json
import requests
from time import sleep
 
def AmzonParser(url):
   # headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    page = requests.get(url)
    while True:
        sleep(3)
        doc = html.fromstring(page.content)
        XPATH_NAME = '//h1[@id="title"]//text()'
        XPATH_SALE_PRICE = '//span[@id="priceblock_ourprice"]/text()'
        XPATH_AVAILABILITY = '//div[@id="availability"]//text()'
        XPATH_COMMENT = '//div[@data-hook="review-collapsed"]//text()'

        RAW_NAME = doc.xpath(XPATH_NAME)
        RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
        RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
        RAW_Comment = doc.xpath(XPATH_COMMENT)

        NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
        SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
        AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None
        Comment = ''.join(RAW_Comment).strip() if RAW_Comment else None

        data = {
                'NAME':NAME,
                'SALE_PRICE':SALE_PRICE,
                'AVAILABILITY':AVAILABILITY,
                'Comment':Comment,
                'URL':url,
                }
        return data

def ReadAsin():
    AsinList = ['B07C7B8F6V',
    'B01FM7GG58',
    'B079VC8RC7',
    'B07D2H23ZN',
    'B07DKZSGFT',
    'B01NBR7VS8',
    'B0789LZTCJ',
    'B06XTV5KZJ',]
    extracted_data = []
    for i in AsinList:
        url = "https://www.amazon.in/dp/"+i
        print("Processing: "+url)
        extracted_data.append(AmzonParser(url))
        sleep(5)
    f=open('data.json','w')
    json.dump(extracted_data,f,indent=4)

if __name__ == "__main__":
    ReadAsin()