from urllib import request
import json

def fetch(URL):
	try:
		response = json.loads(
			request
				.urlopen(URL)
				.read()
				.decode("utf-8")
			)
		return response
	except:
		return