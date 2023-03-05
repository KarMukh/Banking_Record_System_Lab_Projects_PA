import Class_Bank
from Art import art


# object1 = Class_Bank.ClientAccount
# obj = Class_Bank.Bank()


def user_page():
    print("Banking Record System")
    print(art)
    # input()


# def write_account():
#     account = Class_Bank.ClientAccount()
#     account.create_account()
#     Class_Bank.write_accounts_file(account)


# ##### ****

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
    print("\n\tPress 'Enter' and select your option from the Menu (1-7)")

    menu_option = input()
    if menu_option == '1':
        Class_Bank.create_account()
    elif menu_option == '2':
        num = int(input("\tEnter the account number: "))
        Class_Bank.deposit_or_withdraw(num, 1)
    elif menu_option == '3':
        num = int(input("\tEnter the account number: "))
        Class_Bank.deposit_or_withdraw(num, 2)
    elif menu_option == '4':
        num = int(input("\tEnter the account number: "))
        Class_Bank.display_result(num)
    elif menu_option == '5':
        Class_Bank.display_all()
    elif menu_option == '6':
        num = int(input("\tEnter the account number: "))
        Class_Bank.delete_account(num)
    elif menu_option == '7':
        print("\tExiting Banking Record System")
        break

    else:
        print("Invalid choice | Select your option from the Menu (1-7)")

    menu_option = input("Press 'Enter' and select your option from the Menu (1-7)")
