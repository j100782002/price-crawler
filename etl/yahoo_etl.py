import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver

from .base_etl import BaseETL

class YahooETL(BaseETL):
    def extract(self):
        # 從yahoo提取網頁原始碼
        browser = webdriver.Chrome()
        url = f"https://tw.buy.yahoo.com/search/product?p={self.encoded_prod_name}"
        browser.get(url)
        for y in range(0, 10000, 500):
            browser.execute_script(f"window.scrollTo(0, {y})")
            time.sleep(0.5)
        html = browser.page_source
        soups = BeautifulSoup(html, 'html.parser')
        browser.quit()
        return soups
    def transform(self, soups):
        # 轉換yahoo的數據格式，提取所需的商品信息
        items =soups.select("div[class*='ResultList_resultList_']")[0].find("ul", class_="gridList").find_all("a")
        # 頁面會藏一些不是商品的連結，只有網址內有gdsale的才是商品
        links = [item["href"] for item in items if "gdsale" in item["href"]]
        # 取得商品的品名、價格、運送方式，一個商品一個字典存進products list
        products = []

        for link in links:
            response = requests.get(link)
            html = response.text
            soup = BeautifulSoup(html, "html.parser")

            product = {}
            product["name"] = soup.select("h1[class*='HeroInfo__title___']")[0].text
            price = soup.select("div[class*='eroInfo__mainPrice___']")[0].text
            float_price = float(price[1:].replace(',',''))
            product["price"] = float_price
            product["link"] = link
            products.append(product)
        return products



