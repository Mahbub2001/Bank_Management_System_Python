from datetime import datetime
from ALL_strings import *
from Person import Person

class User(Person):
    def __init__(self, name, email, account_type):
        self.is_saving, self.__acc_num, self.__balance, self.__password = account_type, None, 0, None
        self.loan_limit, self.__transaction_history = 0, []
        super().__init__(name, email)

    def __repr__(self):
        print(f"USER NAME : {self.name}\n USER EMAIL :  {self.email}\n USER BALANCE: {self.show_balance}")
        return ""
    
    def set_account_number(self, number):
        self.__acc_num = number

    def password_change(self, password): 
        self.__password = password

    def password_matching(self, password):
        return self.__password == password    
    
    def create_account(self, bank, password):
        return bank.create_account(self, password)
    
    @property
    def account_number(self):  
        return self.__acc_num

    def add_money(self, amount): 
        self.__balance += amount
        self.__transaction_history.append(TRANSACTION_ADD_AMOUNT.format(amount=amount, date=datetime.now().date(), hour=datetime.now().hour, minute=datetime.now().minute)) 

    def deposit(self, amount, bank):
        bank.add_balance(amount)
        self.__balance += amount
        self.__transaction_history.append(TRANSACTION_DEPOSIT.format(amount=amount, date=datetime.now().date(), hour=datetime.now().hour, minute=datetime.now().minute))
        return f"RECEIVING AMOUNT :  {amount} TK. NOW TOTAL BALANCE IS :  {self.__balance}"

    def withdraw(self, amount, bank):
        if amount > self.__balance:
            return "YOU HAVEN'T ENOUGH MONEY TO WITHDRAW"
        elif amount < 100 or not bank.has_money(amount):
            return f"YOU CAN NOT WITHDRAW LESS THAN 100 TK"
        elif bank.is_bankrupt:
            return BANKRUPT_MESSAGE
        else:
            self.__balance -= amount
            bank.cut_balance(amount)
            self.__transaction_history.append(TRANSACTION_WITHDRAW.format(amount=amount, date=datetime.now().date(), hour=datetime.now().hour, minute=datetime.now().minute)) 
            return f"SUCCESSFULLY WITHDRAW AMOUNT : {amount} TK"

    def view_transaction_history(self):
        for tans in self.__transaction_history:
            print(tans)

    @property
    def available_balance(self): 
        return self.__balance
    
    @property
    def show_balance(self): 
        return self.__balance
    
    def take_loan(self, bank, amount): 
        if bank.loan_feature and self.loan_limit < 2 and 5000 <= amount <= 100000 and bank.has_money(amount):  
            self.loan_limit += 1
            self.__balance += amount
            bank.cut_balance(amount)
            bank.add_loan(amount)
            self.__transaction_history.append(TRANSACTION_LOAN.format(amount=amount, date=datetime.now().date(), hour=datetime.now().hour, minute=datetime.now().minute))
            return f"YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREDITED : {amount}TK. YOUR CURRENT BALANCE IS :  {self.__balance}"
        else:
            return LOAN_LIMIT_EXCEEDED

    def transfer_money(self, amount, sender_account_number, bank):
        if bank.is_bankrupt:
            return BANKRUPT_MESSAGE
        if bank.get_user_n(sender_account_number) and self.__balance >= amount:
            self.__balance -= amount
            bank.cut_balance(amount)
            bank.sent_money(sender_account_number, amount)
            self.__transaction_history.append(TRANSACTION_TRANSFER.format(amount=amount, account_number=sender_account_number, date=datetime.now().date(), hour=datetime.now().hour, minute=datetime.now().minute))
            return TRANSFER_SUCCESS.format(amount=amount, account_number=sender_account_number, balance=self.__balance)
        else:
            return f"{sender_account_number} THIS ACCOUUNT DOES NOT EXIST OR YOU HAVE NOT ENOUGH MONEY"

    

