from Person import Person

class Admin(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__acc_num = None
        self.__password = None

    def password_matching(self, password): 
        return self.__password == password
    
    def create_account(self, password, bank):
        return bank.create_admin_account(self,password)
    
    
    @property
    def account_number(self): 
        return self.__acc_num

    def set_account_number(self, number): 
        self.__acc_num = number

    def declare_bankrupt(self, bank):
        bank.bankrupt(self)

    def password_change(self, password): 
        self.__password = password

    def total_bank_balance(self, bank):
        return bank.total_balance 

    def total_loan(self, bank):  
        return bank.total_loan() 

    def delete_users_account(self,bank):
        bank.delete_users_account()

    def see_all_users(self, bank):
        bank.show_all_users()

    def change_feature_loan_type(self, bank, change_with):
        bank.change_feature_loan_type(self, change_with)