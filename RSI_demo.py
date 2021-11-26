import pandas as pd
import shioaji as sj
from dotenv import load_dotenv
import os, threading
import numpy as np
import time
from datetime import datetime

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
contracts = [api.Contracts.Stocks['2330']]


def RSI(close, period=12):
    # 整理資料
    Close = close[-13:]
    Chg = Close - Close.shift(1)
    Chg_pos = pd.Series(index=Chg.index, data=Chg[Chg > 0])
    Chg_pos = Chg_pos.fillna(0)
    Chg_neg = pd.Series(index=Chg.index, data=-Chg[Chg < 0])
    Chg_neg = Chg_neg.fillna(0)

    # 計算平均漲跌幅度
    up_mean = np.mean(Chg_pos.values[-12:])
    down_mean = np.mean(Chg_neg.values[-12:])

    # 計算 RSI
    if (up_mean + down_mean > 0):
        rsi = 100 * up_mean / (up_mean + down_mean)
    else:
        rsi = -1

    return rsi


minute_close = pd.Series()
stock = 0

# 紀錄前12個close
for i in range(0, 12):
    snapshots = api.snapshots(contracts)
    minute_close = minute_close.append(pd.Series(
        [snapshots[0].close],
        index=[pd.to_datetime(snapshots[0].ts, unit='ns')]
    ))
    time.sleep(60)

# 開始算RSI
for i in range(0, 700):
    # 抓snapshot
    snapshots = api.snapshots(contracts)

    # 存到分k收盤價的series
    minute_close = minute_close.append(pd.Series([snapshots[0].close],
                                                 index=[pd.to_datetime(snapshots[0].ts, unit='ns')]))

    # 計算rsi
    rsi = RSI(minute_close)
    # 觸發訊號判斷
    if rsi <= 30 and rsi >= 0 and stock == 0:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time, "BUY AT ", snapshots[0].close)
        stock += 1
    if rsi >= 70 and stock == 1:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time, "SELL AT ", snapshots[0].close)
        stock -= 1
    time.sleep(60)


