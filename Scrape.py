from bs4 import BeautifulSoup
import requests
from Product import Product
from tqdm import tqdm
import numpy as np
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
        
        products = Scrape.searchProductInfo(productLinks)
        return products
    

    def searchProductInfo(productLinks):
        
        #プログレスバー
        bar = tqdm(total = len(productLinks))

        products = np.array([])
        for i in range(len(productLinks)):
            bar.update(1)
            #リンク取得
            link = productLinks[i]
            res = requests.get(link)
            soup = BeautifulSoup(res.text, 'html.parser')
            #商品名
            try:
                name = soup.select_one("#productTitle").getText()
            except:
                name = "null"
            
            #金額
            try:
                price = soup.select_one("span.a-price-whole").getText()
            except:
                price = -1
         
            #レビュー数
            try:
                reviewCount = soup.select_one("span#acrCustomerReviewText").getText()
            except:
                reviewCount = "null"
            
            #評価
            try:
                productValue = soup.select_one(".a-icon-alt").getText()
            except:
                productValue = "null"    
            
            #Productに詰める
            if(name != "null" and price != -1 and reviewCount != "null" and productValue and "null"):
                product = Product()
                product.name = name
                product.price = price
                product.reviewCount = reviewCount
                product.productValue = productValue
                product.URL = link
                 
                products = np.append(products, product)
            
            time.sleep(1)
        
        return products




