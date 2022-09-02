# Write a new function to print a ‘cashier receipt’ output for a shop (any shop – clothes, food, 
# events etc). It should accept 3 items, then sum them up and print out a detailed receipt with 
# TOTAL.


import tabulate

from tabulate import tabulate

print('Hello and welcome to the CFG Store. \n')

item_1_name = input('What is the name of your first item you would like to buy? ')
item_1_price = float(input('What is the price of your item - {}? '.format(item_1_name)))
item_2_name = input('\nWhat is the name of your second item you would like to buy?')
item_2_price = float(input('What is the price of your item - {}? '.format(item_2_name)))
item_3_name = input('\nWhat is the name of your third item you would like to buy? ')
item_3_price = float(input('What is the price of your item - {}?'.format(item_3_name)))
price_total = (item_1_price + item_2_price + item_3_price)

receipt = [
    [item_1_name, item_1_price],
    [item_2_name, item_2_price],
    [item_3_name, item_3_price],
    ["TOTAL", price_total],
    ]

head = ["Item", "Price"]

print('\nHere is a detailed receipt of your purchases:')

print(tabulate(receipt, headers=head, tablefmt="grid"))

print ('Thank you for shopping with us today.')
