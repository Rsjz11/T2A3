#!/usr/bin/python3

from prettytable import PrettyTable

#def Crypto_wallet_table():
table = PrettyTable()

table.field_names = ["Cryptocurrency", "Price", "Quantity", "Total", "Daily (+/-) %", "Weekly (+/-) %"]

table.add_row(["Bitcoin", 5000, 10, 50000, 10, 15])
table.add_row(["Ethereum", 300, 35, 10500, 10, 20])
table.add_row(["Powerledger", 0.10, 10000, 1000, 5, 10])
table.add_row(["Neo", 20, 100, 2000, 3, 5])
table.add_row(["Monero", 100, 50, 5000, 5, 15])

print(table)

def Cryptocurrency():
    pass

def Price():
    pass

def Quantity():
    pass

def Total():
    pass

def Daily_Percentage_Change():
    pass

def Weekly_Percentage_Change():
    pass