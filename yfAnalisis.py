import pandas as pd
import yfinance as yf
from typing import Literal

def fetchData(symbol:str, column:Literal['Open', 'High', 'Low', 'Close', 'Volume','Dividends', 'Stock Splits']=None):
	dat = yf.Ticker(symbol)

	dat = dat.history(period='1y', interval="1wk")
	if column:
		dat = dat[column]

	print(dat)
	
	#dat.to_excel('Analisis.xlsx', index=False)

fetchData("NOMD", column='Dividends')