"""
Description: {Developing a program to process account data to determine interest earned.}
Author: {Gaganpreet Kaur}
Date: {October 3, 2024}
"""

# IMPORT STATEMENTS
from pprint import pprint


dictionary = {}
with open("account_balances.txt" , "r") as file:
    for read_mode in file:
        key, value = read_mode.strip().split('|')
        dictionary[key] = float(value)

pprint(dictionary)