import re
import pandas as pd
import yfinance as yf
from typing import Literal


def calculatePeriod(intervalo:Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1d", "5d", "1wk", "1mo", "3mo"], cantidad=int):
	timeStrInterval = re.sub(r'\d+', '', intervalo)

	#intervalo possibilities are: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1d, 5d, 1wk, 1mo, 3mo
	intervalMap = {'1m': 1, '2m': 2, '5m': 5, '15m': 15, '30m': 30, '60m': 60, '90m': 90, '1d': 1440, '5d': 7200, '1wk': 10080, '1mo': 43800, '3mo': 131400}
	intervalMinutes = intervalMap[intervalo]
	intervalQuantity = intervalMinutes * cantidad

	#period possibilities are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
	convPrd = [1440, 7200, 43800, 131400, 262800, 525600, 1051898, 2629746, 5259492]
	prdMap = {1440: '1d', 7200: '5d', 43800: '1mo', 131400: '3mo', 262800: '6mo', 525600: '1y', 1051898: '2y', 2629746: '5y', 5259492: '10y'}
	#update later to use only the dict and not the list, but for now it is easier to use the list to compare the interval quantity with the period possibilities
	
	for prd in convPrd:
		print(f"interval: {intervalQuantity} period: {prd}")
		if intervalQuantity <= prd:
			returnedPrd = prdMap[prd]
			return [intervalQuantity, returnedPrd]

		
			
print(calculatePeriod("1mo", 6))
		

	#calculate the period to fetch data based on the interval and cantidad

	



def fetchData(symbol=str,intervalo=str, cantidad=int):
	dat = yf.Ticker(symbol)

		
	Interval_Period = calculatePeriod(intervalo, cantidad)

	dat = dat.history(period=Interval_Period[1], interval=intervalo)
	dat = dat["Close"]
	print(dat)
	dat.to_excel('Analisis.xlsx', index=False)

fetchData("NOMD", "1mo", 6)