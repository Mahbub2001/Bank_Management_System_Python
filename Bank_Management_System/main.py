from ALL_strings import *
from Bank_Managment import Bank
from Admin import Admin
from Users import User

EBL = Bank("EBL", "Dhaka", "info@ebl-bd.com")

def user_menu(user, EBL):
    while True:
        print(WELCOME_USER.format(name=user.name.upper()))
        print("Choose 1: DEPOSIT\nChoose 2: WITHDRAW\nChoose 3: AVAILABLE BALANCE\nChoose 4: TRANSACTION HISTORY\nChoose 5: TRANSFER MONEY\nChoose 6: GETTING LOAN!!\nChoose 7: EXIT\n")
        choice = int(input("Enter your preferable option :"))

        if choice == 1:
            amount = int(input(DEPOSIT_PROMPT))
            print(user.deposit(amount, EBL))
        elif choice == 2:
            amount = int(input(WITHDRAW_PROMPT))
            print(user.withdraw(amount, EBL))
        elif choice == 3:
            print(BALANCE_MESSAGE.format(balance=user.available_balance))
        elif choice == 4:
            user.view_transaction_history()
        elif choice == 5:
            id_sender = input(TRANSFER_PROMPT_SENDER)
            amount = int(input(TRANSFER_PROMPT_AMOUNT))
            print(user.transfer_money(amount, id_sender, EBL))
        elif choice == 6:
            amount = int(input("Enter your expected loan amount : "))
            print(user.take_loan(EBL, amount))
        elif choice == 7:
            break
        else:
            print(INVALID_INPUT_MESSAGE)

def admin_menu(admin, EBL):
    while True:
        print(WELCOME_ADMIN.format(name=admin.name.upper()))
        print(SEE_ALL_USERS + DELETE_USER_ACCOUNT + TOTAL_BANK_BALANCE + TOTAL_LOAN_AMOUNT + CHANGE_LOAN_FEATURE + LOGOUT_ADMIN)
        choice = int(input("Enter Option : "))
        if choice == 1:
            admin.see_all_users(EBL)
        elif choice == 2:
            admin.delete_users_account(EBL)
        elif choice == 3:
            print("Total balance : ", admin.total_bank_balance(EBL))
        elif choice == 4:
            print("Total loan amount :  ", admin.total_loan(EBL))
        elif choice == 5:
            selc = int(input("Choose 1: STOP \nChoose 2: \nCONTINUE : "))
            if selc in [1, 2]:
                admin.change_feature_loan_type(EBL, bool(selc - 1))
            else:
                print(INVALID_INPUT_MESSAGE)
        elif choice == 6:
            break
        else:
            print(INVALID_INPUT_MESSAGE)

def main():
    while True:
        print(WELCOME_BANK + LOGIN_MENU)
        choice = int(input("\nEnter your preferable option :"))
        if choice == 1:
            print("\n----------------------------------USER LOGIN-----------------------------------\n")
            account = input("Enter your correct account number :")
            password = input("Enter your correct account password :")
            if EBL.is_user(account, password):
                user = EBL.return_user_account(account)
                user_menu(user, EBL)
            else:
                print(USER_LOGIN_ERROR)
        elif choice == 2:
            print("\n----------------------------------ADMIN LOGIN-----------------------------------\n")
            account = input("Enter your correct account number : ")
            password = input("Enter your correct password :")
            if EBL.is_admin(account, password):
                admin = EBL.return_admin_account(account)
                admin_menu(admin, EBL)
            else:
                print(ADMIN_LOGIN_ERROR)
        elif choice == 3:
            print("\n----------------------------------USER CREATE ACCOUNT-----------------------------------\n")
            name = input("Enter your name :")
            email = input("Enter your email :")
            print("Select Account Type")
            print("Choose 1 : CURRENT ACCOUNT \nChoose 2 : SAVINGS ACCOUNT")
            options = int(input("Enter your preferable account type :"))
            if options in [1, 2]:
                password = input("Input a strong password : ")
                user = User(name, email, bool(options - 1))
                print(user.create_account(EBL, password))
        elif choice == 4:
            print("\n----------------------------------ADMIN CREATE ACCOUNT-----------------------------------\n")
            name = input("Enter your name :")
            email = input("Enter your email :")
            admin = Admin(name, email)
            password = input("Enter a password :")
            print(admin.create_account(password, EBL))
        elif choice == 5:
            break
        else:
            print(INVALID_INPUT_MESSAGE)

if __name__ == "__main__":
    main()
