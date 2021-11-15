
from shioaji.data import Kbars
import pandas as pd
import shioaji

api = shioaji.Shioaji(simulation=True)  # simulation 測試帳號
person_id = 'PAPIUSER01'
passwd = '2222'  # 正式使用要把id改身分證字號, 密碼改永豐密碼

api.login(person_id=person_id, passwd=passwd,
          contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done."))


accounts = api.list_accounts()

kbars = api.kbars(api.Contracts.Stocks["0050"], start="2010-01-01", end="2021-09-02")  # k棒
df = pd.DataFrame({**kbars})
