from checks import *
from frankfurter import *

inputData = input("Date(YYYY-MM-DD) CURRENCY1 CURRENCY2: ")

isArgumentsValid, argumentsError = validateArguments(inputData)

if not(isArgumentsValid):
	print(argumentsError)
else:
	date, currency1, currency2 = inputData.split(" ")
	isDateValid, dateError = validateDate(date)
	
	currencies = getCurrencies()
	isCurrencyValid, currencyError = validateCurrency(currencies, currency1, currency2)
	
	if not(isDateValid):
		print(dateError)
	elif not(isCurrencyValid):
		print(currencyError)
	else:
		try:
			rate, inverseRate = getConversionRate(date, currency1, currency2)
		except:
			print("There is an error with Frankfurter API.")
		else:
			print(f"The conversion rate on {date} from {currency1} to {currency2} was {rate}. The inverse rate was {inverseRate}")
		
# 2021-07-16 GBP AUD