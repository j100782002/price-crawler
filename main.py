from etl.momo_etl import MomoETL
from etl.pchome_etl import PChomeETL
from etl.yahoo_etl import YahooETL


def main():
    product = input("請輸入要搜尋的商品: ")
    
    etl_list = [
        YahooETL(product),
        MomoETL(product),
        PChomeETL(product)
    ]
    
    for etl in etl_list:
        etl.process()

if __name__ == "__main__":
    main()
    print("已完成")