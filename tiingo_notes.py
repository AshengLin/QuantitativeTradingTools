import os
import pandas_datareader as pdr
from dotenv import load_dotenv

SPY = pdr.get_data_tiingo('SPY', api_key=os.getenv('YOUR_TIINGO_KEY'))
print(SPY)