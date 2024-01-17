import random
from datetime import datetime
from ALL_strings import *

class Bank:
    def __init__(self, name, address, email) -> None:
        self.name, self.address, self.email = name, address, email
        self.__users, self.bankrupt, self.__admins = {}, True, {}
        self.__total_balance, self.__is_bankrupt = 5000000000, False
        self.__email_admin, self.__loan_feature = [], True
        self.__loan, self.__users_email = 0, []

    def create_account(self, user, password):
        if user.email in self.__users_email:
            return UNAVAILABLE_EMAIL
        elif user.account_number is None:
            account_number = f"{random.randint(1, 100)}-{user.name[:3]}-{random.randint(10, 1000)}-{int(user.is_saving)}"
            user.set_account_number(account_number)
            self.__users[user.account_number] = user
            user.password_change(password)
            self.__users_email.append(user.email)
            return ACCOUNT_CREATED_USER.format(account_number=account_number)
        else:
            return ACCOUNT_ALREADY_EXISTS

    def create_admin_account(self, admin, password):
        if admin.email in self.__email_admin:
            return EMAIL_ALREADY_IN_USE
        elif admin.account_number is None:
            id = f"ADMIN-{admin.name[:3]}-{random.randint(1, 100)}-{random.randint(100, 1000)}-EBL"
            admin.password_change(password)
            admin.set_account_number(id)
            self.__admins[admin.account_number] = admin
            return ACCOUNT_CREATED_ADMIN.format(account_number=id)
        else:
            return EMAIL_ALREADY_IN_USE

    @property
    def is_bankrupt(self):
        return self.__is_bankrupt

    def is_user(self, account_number, password):
        return account_number in self.__users and self.__users[account_number].password_matching(password)

    def return_user_account(self, account_number):
        return self.__users[account_number]
    
    def get_user_n(self, account_number):
        return account_number in self.__users

    def is_admin(self, account_number, password):
        return account_number in self.__admins and self.__admins[account_number].password_matching(password)

    def sent_money(self, sender_account, amount):
        self.__users[sender_account].add_money(amount)

    def return_admin_account(self, account_number):
        return self.__admins[account_number]

    def add_balance(self, amount):
        if amount > 100:
            self.__total_balance += amount
            if self.__is_bankrupt:
                self.__is_bankrupt = False

    def has_money(self, money):
        return money <= self.__total_balance

    def cut_balance(self, amount):
        self.__total_balance -= amount
        if self.__total_balance < 100:
            self.__is_bankrupt = True

    @property
    def total_balance(self):
        return self.__total_balance

    def total_loan(self):
        return self.__loan

    def delete_users_account(self):
        if not self.__users:
            print(NO_USER_AVAILABLE_TO_DELETE)
        elif len(self.__users) == 1:
            self.__users.clear()
            print(ACCOUNT_DELETION_SUCCESS)
        else:
            user_account_with_min_balance = min(self.__users, key=lambda u: self.__users[u].available_balance)
            self.__users.pop(user_account_with_min_balance)
            print(ACCOUNT_DELETION_SUCCESS)

    @property
    def loan_feature(self):
        return self.__loan_feature

    def change_feature_loan_type(self, admin, change):
        if admin.account_number is None:
            print("AT FIRST CREATE YOUR ACCOUNT AS ADMIN")
        else:
            self.__loan_feature = change

    def add_loan(self, amount):
        self.__loan += amount

    def show_loan_balance(self, admin):
        if admin.account_number in self.__admins:
            print(f"TOTAL GIVEN LOAN : {self.__loan}")
        else:
            print("YOUR GIVEN INFORMATION IS NOT CORRECT")

    def show_all_users(self):
        print("\n----- User List -----\n")
        for idx, user in enumerate(self.__users.values(), start=1):
            print(f"SERIAL NUMBER: {idx}")
            print(f"USER NAME: {user.name}")
            print(f"USER EMAIL: {user.email}")
            print(f"ACCOUNT NUMBER: {user.account_number}")
            print(f"ACCOUNT TYPE: {'SAVINGS' if user.is_saving else 'CURRENT'}")
            print(f"BALANCE: {user.available_balance} TK")
            print("-------------------------------\n")

