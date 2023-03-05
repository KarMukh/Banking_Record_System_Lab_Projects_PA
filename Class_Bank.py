import pickle
import os
import pathlib

accounts_list = []


class ClientAccount:
    name = ""
    surname = ""
    account_number = 0
    balance = 0
    amount = 0
    # info = ""
    # accounts_list = []

    def __int__(self, name, surname, account_number, amount, balance):
        self.name = name
        self.surname = surname
        self.account_number = account_number
        self.balance = balance
        self.amount = amount
        # self.info = info
        # self.accounts_list = accounts_list

    # def show_client_details(self):
    #     print("Client's details: \n\n")
    #     print("Name: ", self.name)
    #     print("Surname: ", self.surname)
    #     print("Account number: ", self.account_number)
    #     # print("Balance: ", self.balance)

    # def create_account(self):
    #     pass

    # Child class
    # class Bank(ClientAccount):
    #     def __init__(self):
    #         self.amount = None
    #         self.balance = None
    #         self.surname = None
    #         self.name = None
    #         self.account_number = None
    #
    #     def __int__(self, name, surname, account_number, balance):
    #         super().__int__(name, surname, account_number, balance)
    #         self.accounts_list = []

    # def create_account(self):
    #     self.account_number = int(input("Enter the account number: "))
    #     self.name = input("Enter the client's name: ")
    #     self.surname = input("Enter the client's surname: ")
    #     print("\n\nAccount created")
    #     self.balance = 0
    #     print("Account balance is: $", self.balance)
    #
    #     self.accounts_list.append(self.account_number)

    def deposit_amount(self, amount):
        self.amount = amount
        self.balance += self.amount
        print("Account balance is: $", self.balance)

    def withdraw_amount(self, amount):
        # ################################ Transfer money to another account = withdraw from one and deposit to another
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient money on the account!")
            print("Account balance is: $", self.balance)
        else:
            self.balance -= self.amount
            print("Account balance is: $", self.balance)


# def write_account(self=None):
#     account = ClientAccount
#     account.create_account(self)
#     write_accounts_file(account)


def create_account():
    # global info
    # global account_number
    account_number = int(input("Enter the account number: "))
    name = input("Enter the client's name: ")
    surname = input("Enter the client's surname: ")
    print("\n\nAccount created")
    balance = 0
    print("Account balance is: $", balance)
    accounts_list.append(account_number)
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        info = pickle.load(infile)
        print(info)
        infile.close()
        os.remove("accounts.txt")
    else:
        print("The file does not exists")

    outfile = open("new_accounts.txt", 'wb')
    pickle.dump(info, outfile)
    outfile.close()
    os.rename("new_accounts.txt", 'accounts.txt')


def display_all():
    # global info
    # global account_number
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        info = pickle.load(infile)

        for item in info:
            print(item.name, " ", item.surname, " ", item.account_number, " ", item.balance)
        infile.close()
    else:
        print("No records to display.")


def display_result(num):
    # global info
    # global account_number
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        info = pickle.load(infile)
        infile.close()
        # found = False

        for item in info:
            if item.account_number == num:
                print("Account balance is = ", item.balance)
                # found = True

            # else:
            #     print() ####################################################
    else:
        print("No records to search.")


def deposit_or_withdraw(num1, num2):
    # global info
    # global account_number
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        info = pickle.load(infile)
        infile.close()

        os.remove("accounts.txt")

        print(info)
    #     for item in info:
    #         if item.account_number == num1:
    #             if num2 == 1:
    #                 amount = int(input("Enter the amount to deposit : "))
    #                 item.balance += amount
    #                 print("Account is updated.")
    #
    #             elif num2 == 2:
    #                 amount = int(input("Enter the amount to withdraw : "))
    #                 if 0 < amount <= item.balance:
    #                     item.balance -= amount
    #                 else:
    #                     print("Insufficient money on the account or wrong number!")
    # else:
    #     print("No records to search.")

    outfile = open("new_accounts.txt", 'wb')
    pickle.dump(info, outfile)
    outfile.close()
    os.rename("new_accounts.txt", 'accounts.txt')


def transfer_money():
    # global info
    # global account_number
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        info = pickle.load(infile)
        infile.close()

        os.remove("accounts.txt")

    while len.accounts_list > 1:
        account_1 = int(input("Please input the account number you want money to transfer from"))
        if account_1 in accounts_list:
            account_2 = int(input("Please input the account number you want money to transfer to"))
            if account_2 in accounts_list:
                transfer_amount = int(input("Please enter the amount you want to transfer"))
                if 0 < transfer_amount <= account_1.balance:
                    account_1.balance -= transfer_amount
                    account_2.balance += transfer_amount
                else:
                    print("Insufficient money on the account or wrong number!")

            else:
                print("The account number does not exists. Please input another one.")
        else:
            print("The account number does not exists. Please input another one.")

    outfile = open("new_accounts.txt", 'wb')

    pickle.dump(info, outfile)

    outfile.close()

    os.rename("new_accounts.txt", 'accounts.txt')


def delete_account(num):
    # global account_number
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        old_list = pickle.load(infile)
        infile.close()
        new_list = []

        for item in old_list:
            if item.account_number != num:
                new_list.append(item)
        os.remove("accounts.txt")
        outfile = open("new_accounts.txt", 'wb')
        pickle.dump(new_list, outfile)
        outfile.close()
        os.rename("new_accounts.txt", 'accounts.txt')


def write_accounts_file(account):
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        old_list = pickle.load(infile)
        old_list.append(account)
        infile.close()
        os.remove("accounts.txt")
    else:
        old_list = [account]
    outfile = open("new_accounts.txt", 'wb')
    pickle.dump(old_list, outfile)
    outfile.close()
    os.rename("new_accounts.txt", 'accounts.txt')
