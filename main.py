import pickle

import os

import pathlib

from Class_Bank import ClientAccount
# from Class_Bank import Bank
from Art import art


# r = 'c:/bro.txt'
# y = 123
# pickle.dump(y, open(r, 'wb'))


# txt_file = 'C:\Users\KarenM\PycharmProjects\Banking_Record_System_Lab_Projects_PA\file.txt'
#
# x = 123
#
# pickle.dump(x, open(txt_file, 'w'))


def check_balance(self):
    self.show_client_details()
    return self.balance


def user_page():
    print("Banking Record System")
    print(art)

    input()


def write_account():
    account = ClientAccount()
    account.create_account()
    write_accounts_file(account)


def display_all():
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        mylist = pickle.load(infile)

        for item in mylist:
            print(item.name," ", item.surname," ", item.account_number," ", item.balance)
        infile.close()
    else:
        print("No records to display.")


def display_result(num):
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False

        for item in mylist:
            if item.account_number == num:
                print("Account balance is = ", item.balance)
                found = True

            # else:
            #     print()
    else:
        print("No records to search.")


def deposit_or_withdraw(num1, num2):
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
    mylist = pickle.load(infile)
    infile.close()

    os.remove("accounts.txt")

    for item in mylist:
        if item.account_number == num1:
            if num2 == 1:
                amount = int(input("Enter the amount to deposit : "))
                item.balance += amount
                print("Account is updated.")

            elif num2 == 2:
                amount = int(input("Enter the amount to withdraw : "))
                if amount <= item.balance:
                    item.balance -= amount
                else:
                    print("Insufficient money on the account!")
    else:
        print("No records to search.")

    outfile = open("newaccounts.txt", 'wb')

    pickle.dump(mylist, outfile)

    outfile.close()

    os.rename("newaccounts.txt", 'accounts.txt')


def delete_account(num):
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []

        for item in oldlist:
            if item.account_number != num:
                newlist.append(item)
        os.remove("accounts.txt")
        outfile = open("newaccounts.txt", 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename("newaccounts.txt", 'accounts.txt')

def write_accounts_file(account):
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove("accounts.txt")
    else:
        oldlist = [account]
    outfile = open("newaccounts.txt", 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename("newaccounts.txt", 'accounts.txt')


# Main part
menu_option = ""
num = 0
user_page()

# menu_option = input("Enter your choice: ")

while menu_option != 7:
    print("\n\tMenu")
    print("\t1. Open new account")
    print("\t2. Deposit amount")
    print("\t3. Withdraw amount")
    print("\t4. Check balance")
    print("\t5. Display all accounts")
    # I need to delete this comment. I put this option to see all the accounts number to transfer money.
    print("\t6. Delete an account")
    print("\t7. Exit")
    print("\tSelect your option from the Menu (1-7)")


    menu_option = input()
    if menu_option == '1':
        write_account()
    elif menu_option == '2':
        num = int(input("\tEnter the account number: "))
        deposit_or_withdraw(num, 1)
    elif menu_option == '3':
        num = int(input("\tEnter the account number: "))
        deposit_or_withdraw(num, 2)
    elif menu_option == '4':
        num = int(input("\tEnter the account number: "))
        display_result(num)
    elif menu_option == '5':
        display_all()
    elif menu_option == '6':
        num = int(input("\tEnter the account number: "))
        delete_account(num)
    elif menu_option == '7':
        print("\tExiting Banking Record System")
        break

    else:
        print("Invalid choice | Select your option from the Menu (1-7)")

    menu_option = input("Enter your choice: ")