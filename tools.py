import shioaji as sj
from dotenv import load_dotenv
import os
import pandas as pd


class QT(object):
    def login(self):
        load_dotenv()
        self.login(person_id=os.getenv('YOUR_PERSON_ID'), passwd=os.getenv('YOUR_PASSWORD'),
                       contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done."))
        accounts = self.list_accounts()
        print('login')
        print(accounts)

    def logout(self):
        self.logout()
        print('logout')

    def k_bar(self, s, e):
        contract = self.Contracts.Stocks['2330']
        k_bars = self.kbars(contract, start=s, end=e)  # Stocks[] 股票, Futures[] 期貨, Options[] 選擇權, Indexs[] 指標
        df = pd.DataFrame({**k_bars})
        df.ts = pd.to_datetime(df.ts)
        return df


    def action(self, p, q, a):
        contract = self.Contracts.Stocks['2330']
        order = self.Order(price=p, quantity=q,
                           action=a,  # sj.constant.Action.Buy, 買進  sj.constant.Action.Sell, #賣出
                           price_type=sj.constant.StockPriceType.LMT,
                           order_type=sj.constant.TFTOrderType.ROD,
                           order_lot=sj.constant.TFTStockOrderLot.Common,
                           account=self.stock_account)
        trade = self.place_order(contract, order)  # 對該contract 進行 order操作
        print(trade)
