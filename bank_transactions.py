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

# Menu Selection Prompt
selected_menu = input("Enter your Selection: ")
selected_menu = selected_menu.upper ()

if selected_menu == "D" or selected_menu == "W" or selected_menu == "Q":
    if selected_menu == "D" or selected_menu == "W":
        value = float(input("Enter amount of transaction: "))

        if  user_account_balance < value and selected_menu == "W":
            print("*" * 40)
            print("INSUFFICIENT FUNDS".center(40," "))
            print("*" * 40)

        elif selected_menu == "D":
         user_account_balance += value
        elif selected_menu == "W":
         user_account_balance -= value
    
        print("*" * 40)
        print(f"Your current balance is: ${user_account_balance:,.2f}".center(40," "))
        print("*" * 40)

    elif selected_menu == "Q":
        print("*" * 40)
        print(f"Your current balance is: ${user_account_balance:,.2f}".center(40," "))
        print("*" * 40)
        
else:
        
         while(not(selected_menu == "D" or selected_menu == "W" or selected_menu == "Q")):
          print("*" * 40)
          print("INVALID SELECTION".center(40," "))
          print("*" * 40)
          selected_menu = input("Enter your Selection: ")
          selected_menu = selected_menu.upper ()
          if (selected_menu == "D" or selected_menu == "W" or selected_menu == "Q"):
            value = float(input("Enter amount of transaction: "))
            print("*" * 40)
            if selected_menu == "D":
               user_account_balance += value
            elif  selected_menu == "W":
               user_account_balance -= value
            print(f"Your current balance is: ${user_account_balance:,.2f}".center(40," "))
            print("*" * 40)
