import abc

class BaseETL(abc.ABC):
    def __init__(self, product):
        self.product = product
    
    def process(self):
        # 執行整個 ETL 流程
        data = self.extract()
        transformed_data = self.transform(data)
        self.load(transformed_data)
    
    @abc.abstractmethod
    def extract(self):
        # 從網站提取原始數據
        pass
    
    @abc.abstractmethod
    def transform(self, data):
        # 轉換和清理提取的數據
        pass
    
    @abc.abstractmethod
    def load(self, data):
        # 將轉換後的數據加載到目標位置（如 Google Sheets）
        pass