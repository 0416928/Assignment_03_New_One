"""
Description: {This program will develop an Automated Teller Machine (ATM) simulator.}
Author: {Gaganpreet Kaur}
Date: {October 3, 2024}
"""
# IMPORT STATEMENTS
import random

collection = ["D" ,"W" ,"Q"]
user_account_balance = float(random.randint(-1000,10000))

# Selection Menu
width = 40
fill_char = " "

print("*" * 40 )
print("PIXELL RIVER FINANCIAL".center(width, fill_char))
print("ATM Simulator".center(40," "))
print(f"Your current balance is: ${user_account_balance:,.2f}".center(40," "))
print(f"Deposit: {collection[0]}".center(40," "))
print(f"Withdraw: {collection[1]}".center(40," "))
print(f"Quit: {collection[2]}".center(40," "))
print("*" * 40)