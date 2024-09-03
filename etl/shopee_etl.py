from .base_etl import BaseETL

class ShopeeETL(BaseETL):
    def extract(self):
        # 從蝦皮網站提取商品數據
        pass
    
    def transform(self, data):
        # 轉換蝦皮的數據格式，提取所需的商品信息
        pass
    
    def load(self, data):
        # 將轉換後的蝦皮數據上傳到 Google Sheets
        pass