import json
import requests
from Global_listings import global_list
from Cryptocurrency_list import crypto_list
from Cryptocurrency_specific import crypto_specific
from Cryptocurrency_specific_listing import crypto_specific_list
from Portfolio import portfolio

#def menu_page():
  #  return ' [1] Enter 1 to retrieve global cryptocurrency information.\n [2] Enter 2 for an entire list of cryptocurrencies. \n [3] Enter 3 to retrieve specific cryptocurrency information. \n [4] Enter 4 to retrieve multiple cryptocurrencies in a list. \n [5] Enter 5 to retrieve porfolio information. \n [6] Press 6 to exit \n\n' 

def menu_1():
    global_list()
    

def menu_2():
    crypto_list()
    

def menu_3():
    crypto_specific()
    


def menu_4():
    crypto_specific_list()
    

def menu_5():
    portfolio()


while True:
    prompt = ' [1] Enter 1 to retrieve global cryptocurrency information.\n [2] Enter 2 for an entire list of cryptocurrencies. \n [3] Enter 3 to retrieve specific cryptocurrency information. \n [4] Enter 4 to retrieve multiple cryptocurrencies in a list. \n [5] Enter 5 to retrieve porfolio information. \n [6] Press 6 to exit \n\n' 
    stringInput = input(prompt)
    choice = int(stringInput)
  #  user_input = int(input())

    if choice == 1:
        menu_1()
    elif choice == 2:
        menu_2()
    elif choice == 3:
        menu_3()
    elif choice == 4:
        menu_4()
    elif choice == 5:
        menu_5()
    elif choice == 6:
        break
    else:
        print('Invalid command')

    
                
menu_page()

# FILE = meaninglesS
# functions + variables = important