from abc import ABC, abstractmethod
from utils import upload_to_sheets

class BaseETL(ABC):
    def __init__(self, product):
        self.product = product
    
    def process(self):
        # 執行整個 ETL 流程
        data = self.extract()
        transformed_data = self.transform(data)
        self.load(transformed_data)
    
    @abstractmethod
    def extract(self):
        # 從網站提取原始數據
        pass
    
    @abstractmethod
    def transform(self, data):
        # 轉換和清理提取的數據
        pass
    
    def load(self, data):
        # 將轉換後的數據加載到 Google Sheets
        upload_to_sheets(data)