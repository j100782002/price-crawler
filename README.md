# price-crawler


## 專案簡介
這個專案讓使用者輸入想購買的產品名稱，程式會自動從 Momo、PChome 和 Yahoo 三個購物網站爬取第一頁的搜尋結果，並將產品名稱、價格及連結抓取下來，最終上傳到 Google Sheets。這樣的工具可以幫助使用者在瀏覽購物網時避免受到其他商品的干擾，專注於最初想購買的產品。

## 目錄結構
- [專案功能](#專案功能)
- [安裝步驟](#安裝步驟)
- [使用方式](#使用方式)


## 專案功能
- 從 Momo、PChome 和 Yahoo 購物網爬取產品的名稱、價格及連結。
- 將這些資訊自動上傳至 Google Sheets。

## 安裝步驟
### 1. 克隆專案到本地

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. 用`pipenv` 安裝依賴
```bash
pipenv install
```

### 3. 啟動虛擬環境
```bash
pipenv shell
```

### 4. 設定 Google Sheets API
此專案需要訪問 Google Sheets，因此使用者需要下載 Google Sheets API 的認證金鑰，並將其放置在專案utils資料夾下：

進入 Google Cloud Console，創建一個專案並啟用 Google Sheets API。
在「認證」頁面創建 OAuth 2.0 憑證，並下載 .json 格式的憑證檔案。
將此檔案重新命名為 Key.json，並放置在專案utils資料夾下。

### 5. 設定google 信箱
在utils資料夾下，新增一個名為email.txt的檔案，並打上信箱(欲接收上傳資料的google雲端硬碟信箱)

### 6. 運行專案
```bash
python main.py
```

## 使用方式

1. 運行後會問你想購買的產品名稱
2. 輸入後會開始爬取資料，並將資料上傳至google雲端硬碟
3. 上傳完成後會說已完成
4. 接著就可以去google雲端硬碟上看到一個名為shop_web_crawler的試算表，裡面會有你剛剛輸入的商品名稱的工作表，裡面會有爬取的商品名稱、價格及連結

