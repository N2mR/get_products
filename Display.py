import sys
from Scrape import Scrape

class Display:
    def searchProductsFromAmazon():
        print("type a kewword you want to search :")
        keyword = sys.stdin.readline()
        products = Scrape.scrapeFromAmazon(keyword)
        print("search results : " + str(len(products)))
        Display.displayProducts(products)

    def displayProducts(products):
        for i in range(len(products)):
            product = products[i]
            print(product.name)
            print(product.price)
            print(product.reviewCount)
            print(product.productValue)
            print(product.URL)
            print("-------------")


Display.searchProductsFromAmazon()