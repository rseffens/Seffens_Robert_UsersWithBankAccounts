class User:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account = BankAccount(int_rate=0.10, balance=0)

    def user_info(self):
        print("First name: ", self.first_name)
        print("Last Name: ", self.last_name)
        print("Email: ", self.email)

    def deposit(self, amount):
        self.account.deposit(amount)
        return self

    def withdrawl(self,amount):
        self.account.withdrawl(amount)
        return self

    def display_account_info(self):
        print(f"{self.first_name} has a balance of: {self.account}")
        return self


    # def greeting(self):
    #     print(f"Hello my name is {self.first_name}!")


class BankAccount:
    # class attribute

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"{self.person} has a balance of: {self.account}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            # balance = balance + balance * interest rate
            self.balance = self.balance + (self.balance * self.int_rate)
        return self
            
