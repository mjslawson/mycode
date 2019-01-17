#!/usr/bin/env python3
from blessings import Terminal
t = Terminal()
print(t.clear())

def yellow_np():
    print(t.bold_black_on_yellow('Print yellow text'))

def yellow_wp(p):
    print(t.bold_black_on_yellow(p))

def trx(p):
    x = t.width - len(p)
    return int(x)

def trcx(p):
    x = (t.width//2) - (len(p)//2)
    return int(x)

def top_right(p):
    with t.location(trx(p), 0):
        yellow_wp(p)

def centered(p):
    with t.location(trcx(p), t.height//2):
        yellow_wp(p)

def prompt_location():
    return t.location(0,t.height-2)

def response_location(p):
    return t.location(len(p) + 1,t.height-2)

def prompt(p):
    with prompt_location():
        p = p + " (q + Enter to quit):"
        print(t.reverse(p),t.clear_eol)
    with response_location(p):
        orders = input()
    return orders

orders = ""
while orders != 'q':
    orders = prompt("Your orders")
    orders
#   top_right(orders)
    centered(orders)
    if orders[:3]=='mtr':
        with t.location(0,3):
            os.system(orders)

yellow_wp("Thanks for all the fish")


#top_right("I want this in the top right!")

#orders = prompt("Prompt at bottom left:")

#yellow_np()

#yellow_wp("I want this to print in YELLOW")

#x = trx("I want this to print in YELLOW")
#print(x)
