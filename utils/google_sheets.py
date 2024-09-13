import gspread
from google.oauth2.service_account import Credentials

def upload_to_sheets(data, prod_name):
    # 設置憑證和授權
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = Credentials.from_service_account_file(r'Key.json', scopes=scopes)

    client = gspread.authorize(creds)
    
    # 嘗試打開名為 'shop_web_crawler' 的試算表，如果不存在則創建
    try:
        sheet = client.open('shop_web_crawler')
    except gspread.SpreadsheetNotFound:
        sheet = client.create('shop_web_crawler')
    
    # 嘗試獲取指定的工作表，如果不存在則創建
    try:
        worksheet = sheet.worksheet(prod_name)
    except gspread.WorksheetNotFound:
        worksheet = sheet.add_worksheet(title=prod_name, rows="1000", cols="3")
    # 將email存在檔案，並讓API的帳號將sheet分享給自己使用的sheets帳號
    with open(r"test\email.txt", 'r') as file:
        email = file.read().strip()
        sheet.share(email, perm_type='user', role='writer')
    # 設置欄位標題
    worksheet.update([['name', 'price', 'link']], 'A1:C1')
    
    # 準備數據以插入工作表
    rows_to_insert = [[item['name'], item['price'], item['link']] for item in data]
    
    # 將數據插入工作表
    worksheet.append_rows(rows_to_insert)
