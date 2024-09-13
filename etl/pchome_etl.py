import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver

from .base_etl import BaseETL
class PChomeETL(BaseETL):
    def extract(self):
        # 從 PChome 網站提取商品數據
        browser = webdriver.Chrome()
        url = f"https://24h.pchome.com.tw/search/?q={self.encoded_prod_name}"
        browser.get(url)
        for y in range(0, 10000, 500):
            browser.execute_script(f"window.scrollTo(0, {y})")
            time.sleep(0.5)
        html = browser.page_source
        soups = BeautifulSoup(html, 'html.parser')
        browser.quit()
        return soups

    def transform(self, soups):
        # 轉換 PChome 的數據格式，提取所需的商品信息
        items =soups.find("div", id="ItemContainer")
        products = []
        for item in items:
            product = {}
            product["name"] = item.find("h5", class_="prod_name").text
            price = item.find("span", class_="price").text
            float_price = float(price[1:].replace(',',''))
            product["price"] = float_price
            product["link"] = "https:"+item.find("a", class_="prod_img")["href"]
            products.append(product)
        return products

