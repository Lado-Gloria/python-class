class Student:
    def __int__(self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name =last_name
        self.age =age
        self.country=country

    def show_full_name(self):
        return f"{self.first_name}  {self.last_name}" 

    def year_of_birth(self):
        year =2023 -self.age
        return f"{self.first_name} you were born in {year}"   
    def show_initial(self):
        return f"{self.first_name[0]} .{self.last_name[0]}"
    
class Car:
    make = "benz"
    def __init__(self,model,color,year):
        self.model =model
        self.color=color
        self.year=year
    def start_engine(self):
        return f"{self.clor} {self.model} has a very good engine"   

    def accelerate(self):
        return f"{self.color} was released in {self.year}" 
    
    def stop(self):
        return f"the{self.medel} has stop at a junctions"
class Fruit:
   
    type =  "category"

    def __init__(self, name, color, taste):
       
        self.name = name
        self.color = color
        self.taste = taste

    def peel(self):
        return f"Peeling the {self.color} {self.name}"

    def eat(self):
        return f"Eating the {self.color} {self.name} with {self.taste} taste"

    def discard(self):
        return f"Discarding the {self.color} {self.name}." 



class Account:
  
    bank_name = "Unknown"

    def __init__(self, account_number, account_holder, balance):
      
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"made a bank deposit of {amount} in the account.your balance is {self.balance}."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount} from the account. New balance is {self.balance}."
        else:
            return "Insufficient balance to withdraw."

    def check_balance(self):
        return f"Current balance in the account is {self.balance}."