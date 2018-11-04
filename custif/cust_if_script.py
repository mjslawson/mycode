#!/usr/bin/env python3

""""
Author: mjslawson

Prints how many entire units of a cryptocurrency can be bought with a user-provided input

"""

def is_number(var):
    """ Checks if value is a number """
    try:
        float(var)
        return True
    except ValueError:
        return False

def main():
    """ Main Program """
    message = 'You can buy and entire: \n' # initial message
    money = input("How much USD would you like to spend on crypto? $")
    btc_price = float(6401) # BTC price
    ltc_price = float(51) # LTC price
    eth_price = float(202) # ETH price

    if is_number(money):

        fiat = float(money) # sets fiat as float

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

main()
