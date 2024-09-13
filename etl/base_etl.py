from abc import ABC, abstractmethod
from utils.google_sheets import upload_to_sheets
import urllib.parse  

class BaseETL(ABC):
    def __init__(self, prod_name):
        self.prod_name = prod_name
        # 將產品名稱轉換成url編碼，方便直接帶入網址
        self.encoded_prod_name = urllib.parse.quote(prod_name)
    
    def process(self):
        # 執行整個 ETL 流程
        data = self.extract()
        transformed_data = self.transform(data)
        self.load(transformed_data, self.prod_name)
    
    @abstractmethod
    def extract(self):
        # 從網站提取原始數據
        pass
    
    @abstractmethod
    def transform(self, data):
        # 轉換和清理提取的數據
        pass
    
    def load(self, data, prod_name):
        # 將轉換後的數據加載到 Google Sheets
        upload_to_sheets(data, prod_name)
