class ClientAccount:
    def __int__(self, name, surname, account_number, balance):
        self.name = name
        self.surname = surname
        self.account_number = account_number
        self.balance = balance

    def show_client_details(self):
        print("Clinet's details: \n\n")
        # print(" ")
        print("Name: ", self.name)
        print("Surname: ", self.surname)
        print("Account number: ", self.account_number)
        # print("Balance: ", self.balance)


# Child class
# class Bank(ClientAccount):
#     def __int__(self, name, surname, account_number):
#         super().__int__(name, surname, account_number)
#         self.balance = 0

    def create_account(self):
        self.account_number = int(input("Enter the account number: "))
        self.name = input("Enter the cilent's name: ")
        self.surname = input("Enter the cilent's surname: ")
        print("\n\nAccount created")
        self.balance = 0
        print("Account balance is: $", self.balance)

    def deposit_amount(self, amount):
        self.amount = amount
        self.balance += self.amount
        print("Account balance is: $", self.balance)

    def withdraw_amount(self, amount):
        # ################################### Transfer money to another account
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient money on the account!")
            print("Account balance is: $", self.balance)
        else:
            self.balance -= self.amount
            print("Account balance is: $", self.balance)
