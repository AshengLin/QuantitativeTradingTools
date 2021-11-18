import shioaji as sj
from tools import QT
from model.RL import Agent

sj_object = sj.Shioaji(simulation=True)
QT.login(sj_object)
print(QT.k_bar(sj_object, "2021-05-15", "2021-11-17"))

# QT.action(sj_object, p=12, q=1, a=sj.constant.Action.Buy)
# QT.action(sj_object, p=12, q=1, a=sj.constant.Action.Sell)

QT.logout(sj_object)

# agent = Agent(df=pre_data, n_feature=n_f, n_hist=n_h)