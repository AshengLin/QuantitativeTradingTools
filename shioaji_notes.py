import pandas as pd
import shioaji as sj
from dotenv import load_dotenv
import os

load_dotenv()  # 讀取設定檔中的內容至環境變數，裡面可以放路徑
api = sj.Shioaji(simulation=True)  # simulation 測試帳號
# person_id = 'PAPIUSER01'
# passwd = '2222'  # 正式使用要把id改身分證字號, 密碼改永豐密碼

api.login(person_id=os.getenv('YOUR_PERSON_ID'), passwd=os.getenv('YOUR_PASSWORD'),
          contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done."))

# result = api.activate_ca(
#     ca_path=os.getenv('YOUR_CA_PATH'),  # 下單電子憑證路徑及檔案名稱
#     ca_passwd=os.getenv('YOUR_CA_PASS'),  # 下單電子憑證密碼
#     person_id=os.getenv('YOUR_PERSON_ID'),  # 身份證字號
# )


accounts = api.list_accounts()


contracts = [api.Contracts.Stocks['2330'], api.Contracts.Stocks['2409']]  # 建立一個Contract的List
# short_stock_sources = api.short_stock_sources(contracts)  # Short Stock Source 查詢股票代碼,或有券張數, 更新時間
snapshots = api.snapshots(contracts)  # 查詢快照
# df = pd.DataFrame(snapshots)
# df.ts = pd.to_datetime(df.ts)

k_bars = api.kbars(api.Contracts.Stocks["2330"], start="2015-09-17",
                   end="2021-11-17")  # Stocks[] 股票, Futures[] 期貨, Options[] 選擇權, Indexs[] 指標
df = pd.DataFrame({**k_bars})
df.ts = pd.to_datetime(df.ts)


order = api.Order(price=12, quantity=1,
                  action=sj.constant.Action.Buy,  # 買進  sj.constant.Action.Sell, #賣出
                  price_type=sj.constant.StockPriceType.LMT,
                  order_type=sj.constant.TFTOrderType.ROD,
                  order_lot=sj.constant.TFTStockOrderLot.Common,
                  account=api.stock_account)
contract = api.Contracts.Stocks['2330']
trade = api.place_order(contract, order)  # 對該contract 進行 order操作
print(trade)

api.logout()  # 登出
