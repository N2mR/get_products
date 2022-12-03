from bs4 import BeautifulSoup
import requests
from Product import Product
import time


class Scrape:

    def scrapeFromAmazon(keyword):
        amazonLink = "https://www.amazon.co.jp/"
        searchQuery = "s?k="
        searchLink = amazonLink + searchQuery +  keyword
        
        res = requests.get(searchLink)
        soup = BeautifulSoup(res.text, 'html.parser')

        #複数の商品のリンクを取得する
        productLinks = []
        getLinks = [url.get('href') for url in soup.select('h2.a-size-mini a.a-link-normal')]
        for i in range(len(getLinks)):
            productLinks.append(amazonLink + getLinks[i])
        
        Scrape.searchProductInfo(productLinks)
    

    def searchProductInfo(productLinks):

        for i in range(len(productLinks)):
            #リンク取得
            link = productLinks[i]
            res = requests.get(link)
            soup = BeautifulSoup(res.text, 'html.parser')
            #商品名
            try:
                name = soup.select_one("#productTitle").getText()
            except:
                name = "null"
            finally:
                print(name)
            
            #金額
            try:
                price = soup.select_one("span.a-price-whole").getText()
            except:
                price = -1
            finally:
                print(price)  
                      
            #レビュー数
            try:
                reviewCount = soup.select_one("span#acrCustomerReviewText").getText()
            except:
                reviewCount = "null"
            finally:
                print(reviewCount) 
            
            #評価
            try:
                productValue = soup.select_one(".a-icon-alt").getText()
            except:
                productValue = "null"
            finally:
                print(productValue)             
            
            #URL
            print(link)
            print("-----------")
            time.sleep(1)

Scrape.scrapeFromAmazon("枕")
