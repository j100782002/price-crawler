from .base_etl import BaseETL

class MomoETL(BaseETL):
    def extract(self):
        # 從 momo 網站提取商品數據
        pass

    def transform(self, data):
        # 轉換 momo 的數據格式，提取所需的商品信息
        pass

    def load(self, data):
        # 將轉換後的 momo 數據上傳到 Google Sheets
        pass