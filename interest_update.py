"""
Description: {Developing a program to process account data to determine interest earned.}
Author: {Gaganpreet Kaur}
Date: {October 3, 2024}
"""

# IMPORT STATEMENTS
from pprint import pprint
import csv

# Display Current Balances
dictionary = {}
with open("account_balances.txt" , "r") as file:
    for read_mode in file:
        key, value = read_mode.strip().split('|')
        dictionary[key] = float(value)

pprint(dictionary)

# Incorporate Transactions
for number,value in dictionary.items():

    if value < 1000 and value > 0:
      rate = value + ((value * 0.01) / 12)
      dictionary[number] = rate

    elif value < 5000 and value >= 1000:
      rate = value + ((value * 0.025) / 12)
      dictionary[number] = rate

    elif value >= 5000:
      rate = value + ((value * 0.05) / 12)
      dictionary[number] = rate

    elif value < 0:
      rate = value + ((value * 0.1) / 12)
      dictionary[number] = rate   

    else:
      rate = value + ((value * 0.1) / 12)
      dictionary[number] = rate 

pprint(dictionary)  

file_name = "updated_balances_GK.csv"

# Write the Updated Data
with open("updated_balances_GK.csv", "w") as new_file:
      new_file.write("Account,Balance")
      for key,value in dictionary.items():
        new_file.write(f"\n{key},{value}")

# Display the Updated Data
with open("updated_balances_GK.csv", "r") as reading_file:
      reader = csv.DictReader(reading_file)
      for row in reader:
        print(row)
