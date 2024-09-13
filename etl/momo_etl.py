from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup

from .base_etl import BaseETL

class MomoETL(BaseETL):
    def extract(self):
        # 從 momo 網站提取商品數據
        browser = webdriver.Chrome()
        url = f"https://www.momoshop.com.tw/search/searchShop.jsp?keyword={self.encoded_prod_name}&_isFuzzy=0&searchType=1"
        browser.get(url)

        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'listArea')))

        html = browser.page_source
        soups = BeautifulSoup(html, 'html.parser')

        browser.quit()
        return soups

    def transform(self, soups):
        # 轉換 momo 的數據格式，提取所需的商品信息
        items =soups.find("div", class_="listArea").find_all("li")
        products = []
        for item in items:
            product = {}
            product["name"] = item.find("h3", class_="prdName").text
            price = item.find("span", class_="price").find("b").text
            float_price = float(price.replace(',',''))
            product["price"] = float_price
            product["link"] = item.find("a", class_="goods-img-url")["href"]
            products.append(product)
        return products

