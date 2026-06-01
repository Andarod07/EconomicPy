import pandas as pd
import yfinance as yf

def angelito(symbol):
	dat = yf.Ticker(symbol)
	#print(dat.history(period='1y', interval="1wk"))
	
	dat = dat.history(period='1y', interval="1wk")
	dat = dat["Close"]
	print(dat)
	dat.to_excel('Analisis.xlsx', index=False)

angelito("NOMD")