from etl import ShopeeETL, MomoETL, PChomeETL

def main():
    product = input("請輸入要搜尋的商品: ")
    
    etl_list = [
        ShopeeETL(product),
        MomoETL(product),
        PChomeETL(product)
    ]
    
    for etl in etl_list:
        etl.process()

if __name__ == "__main__":
    main()