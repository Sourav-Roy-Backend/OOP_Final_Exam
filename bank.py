class User:
    
    def __init__(self) -> None:
        self.__u_wallet = 0
        self.__t_withdraw = 0
        self.__t_deposit = 0
        self.__t_transfer = 0
        self.__t_reciev = 0
        self.__t_loan = 0

        
    
    def create_account(self,email,password):
        self.email = email
        self.password = password

    
    def deposit(self,amount):
        self.__u_wallet += amount
        self.__t_deposit += amount
        self.admin = Admin()
        self.admin.add_blance(amount)
    
    def withdraw(self,amount):

        if amount <= self.__u_wallet:
            self.__u_wallet = self.__u_wallet - amount
            self.__t_withdraw += amount
        else:
            print("Bank is Bankrupt")
        
    
    def check_blance(self):
        print(f'Your availavle blance is : {self.__u_wallet}')


    def add_wallet(self,amount):
        self.__u_wallet += amount

    def add_reciev(self,amount):
        self.__t_reciev += amount

   


    
    
    def check_transaction_history(self):
        print(f'Your total deposit is : {self.__t_deposit} and your total withdraw is : {self.__t_withdraw} and total transfer {self.__t_transfer} total reciev {self.__t_reciev} you take loan {self.__t_loan}')

    
    def transfer(self,reciev,amount):
        if amount <= self.__u_wallet:
            self.__u_wallet -= amount
            reciev.add_wallet(amount)
            self.__t_transfer += amount
            reciev.add_reciev(amount)


    def take_loan(self,amount):
        self.admin =Admin()
        b_blance = self.admin.b_blance

        if amount <= self.__u_wallet*2 and amount > b_blance:
            self.__u_wallet += amount
            self.bank = Admin()
            self.bank.b_blance -= amount
            self.__t_loan += amount
            self.loan = Loan()
            self.loan.loan_blance += amount
        else:
            print(f'you cannot take loan ',amount )



            




class Loan:
    def __init__(self) -> None:
        self.loan_blance = 0
    




class Admin:
    def __init__(self) -> None:
        self.b_blance = 1000000
    
   
    def add_blance(self,amount):
        self.b_blance += amount
    

    def create_account(self,email,code):
        self.email = email
        self.code = code
    
  
    def check_bank_blance(self):
        print(f'Avilable bank blance is : {self.b_blance}')

    def check_loan_amount(self):
        self.amount = Loan()
        print(f'Total Loan Amount : {self.amount.loan_blance}')





# user_1 = User()
# user_1.create_account("souravray9001@gmail.com",1234)
# user_1.deposit(2000)
# user_1.take_loan(3000)
# # user_1.check_blance()
# user_1.withdraw(4000)
# user_1.check_blance()
# user_1.check_transaction_history()
# user_2 = User()
# user_2.create_account("banglai34@gmail.com",4325)
# user_2.deposit(1000)
# user_2.check_blance()
# user_2.withdraw(500)
# user_2.check_blance()
# user_2.check_transaction_history()
# user_1.transfer(user_2,1500)

# user_1.check_blance()
# user_2.check_blance()

# user_1.check_transaction_history()
# user_2.check_transaction_history()

user_1= User()
user_1.create_account("souravray9001@gmail.com",1234)
user_1.deposit(2000)
user_1.check_blance()
user_1.take_loan(3000)
user_1.withdraw(4000)
user_1.check_blance()
user_1.check_transaction_history()

user_2= User()
user_2.create_account("omresh01@gmail.com",76544)
user_2.deposit(10000)
user_2.check_blance()
user_2.take_loan(30000)
user_2.withdraw(20000)
user_2.check_blance()
user_2.check_transaction_history()

user_1.transfer(user_2,1500)

db= Admin()
db.create_account("db34@gmail.com",9854332)
db.check_bank_blance()
db.check_loan_amount()
    
        

