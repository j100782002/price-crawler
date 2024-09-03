from .base_etl import BaseETL

class PChomeETL(BaseETL):
    def extract(self):
        # 從 PChome 網站提取商品數據
        pass

    def transform(self, data):
        # 轉換 PChome 的數據格式，提取所需的商品信息
        pass

    def load(self, data):
        # 將轉換後的 PChome 數據上傳到 Google Sheets
        pass