import re
import pandas as pd
import yfinance as yf

def calculatePeriod(intervalo=str, cantidad=int):
	timeStrInterval = re.sub(r'\d+', '', intervalo)

	#intervalo possibilities are: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1d, 5d, 1wk, 1mo, 3mo
	convIntrvl = [1,2,5,15,30,60,90,1440, 7200, 10080, 43800, 131400]
	#period possibilities are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
	convPrd = [1440, 7200, 43800, 131400, 262800, 525600, 1051898, 2629746, 5259492]

	match timeStrInterval:
		
		
		#calculate the period to fetch data based on the interval and cantidad
		#if the interval is in minutes, the period will be in days

		case 'm':
			calculoPeriodo = '???'

	return calculoPeriodo

def fetchData(symbol=str,intervalo=str, cantidad=int):
	dat = yf.Ticker(symbol)

		
	periodo = calculatePeriod(intervalo, cantidad)

	dat = dat.history(period=periodo, interval=intervalo)
	dat = dat["Close"]
	print(dat)
	#dat.to_excel('Analisis.xlsx', index=False)

fetchData("NOMD", "1mo", "1wk")