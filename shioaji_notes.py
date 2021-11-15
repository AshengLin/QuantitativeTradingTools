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

accounts = api.list_accounts()

k_bars = api.kbars(api.Contracts.Stocks["0050"], start="2010-01-01", end="2021-09-02")  # k棒
df = pd.DataFrame({**k_bars})

api.logout()  # 登出
