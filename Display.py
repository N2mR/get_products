import sys
from Scrape import Scrape

class Display:
    def searchProductsFromAmazon():
        print("type a kewword you want to search :")
        keyword = sys.stdin.readline()
        scrape = Scrape()
        scrape.scrapeFromAmazon(keyword)

    def displayProducts():
        return 0
