#!/usr/bin/env python3
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
message = 'You can buy and entire: \n'
money = input("How much USD would you like to spend on crypto? $")
btc_price = float(6401)
ltc_price = float(51)
eth_price = float(202)

if is_number(money):

	fiat = float(money)

	if fiat >= 6401:
		message = message + str(round(fiat/btc_price, 8)) + ' Bitcoin \n'    		
		message = message + str(round(fiat/eth_price, 8)) + ' Ether \n'
		message = message + str(round(fiat/ltc_price, 8)) + ' Litecoin \n'
	elif fiat >= 202:
		message = message + str(round(fiat/eth_price, 8)) + ' Ether \n'
		message = message + str(round(fiat/ltc_price, 8)) + ' Litecoin \n'
	elif fiat >= 51:
		message = message + str(round(fiat/ltc_price, 8)) + ' Litecoin \n'
	else:
		message = 'Sorry, you cannot buy an entire Bitcoin, Ether or Litecoin.'

	print(message)
else:
	print('Ummm, you want to spend ' + money + ' on cryptocurrency?  Try again.')