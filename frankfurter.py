from api import fetch

def getCurrencies():
	currenciesURL = f"https://www.frankfurter.app/currencies/"
	currencies = fetch(currenciesURL)
	if not(currencies): return
	return currencies

def getConversionRate(date, currency1, currency2):
	URL = f"https://www.frankfurter.app/{date}?amount=1&from={currency1}&to={currency2}"
	response = fetch(URL)
	if not(response): return
	rate= response["rates"][currency2]
	inverseRate = round(1/rate, 4)
	return rate, inverseRate