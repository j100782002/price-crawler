import requests
from bs4 import BeautifulSoup
from base_etl import BaseETL

class YahooETL(BaseETL):
    def extract(self):
        # 從yahoo提取網頁原始碼
        url = self.url
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        return soup
    def transform(self, soups):
        # 轉換yahoo的數據格式，提取所需的商品信息
        items = soups.find("div", class_="main").find("ul", class_="gridList").find_all("a")
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
            product["deliver"] = soup.find("div",id="panelButton_PANEL_DELIVERY").text
            products.append(product)
        return products


# test
if __name__ == "__main__":
    url = "https://tw.buy.yahoo.com/search/product?p=samsung+galaxy+s24"
    yahoo_etl = YahooETL(url)
    html =yahoo_etl.extract()
    products = yahoo_etl.transform(html)
    print(products)

