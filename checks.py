from datetime import datetime

def validateArguments(inputs):
	isValid = False
	error = ""
	try:
		date, currency1, currency2 = inputs.split(" ")
		isValid = True
	except:
		error = "[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>."
	return (isValid, error)


def validateDate(date_text):
	isDateValid = False
	error = "Provided date is invalid."
	try:
		isDateValid = bool(datetime.strptime(date_text, '%Y-%m-%d'))
	except:
		isDateValid = False
	return (isDateValid, error)


def validateCurrency(currencies, currency1, currency2):
	error = ""
	isCurrencyValid = False
	if not(currencies):
		error = "There is an error with Frankfurter API."
	elif (currency1 not in currencies) and (currency2 not in currencies):
		error = f"{currency1} and {currency2} is not a valid currency code."
	elif (currency1 not in currencies):
		error = f"{currency1} is not a valid currency code."
	elif (currency2 not in currencies):
		error = f"{currency2} is not a valid currency code."
	else:
		isCurrencyValid = True
	return (isCurrencyValid, error)
