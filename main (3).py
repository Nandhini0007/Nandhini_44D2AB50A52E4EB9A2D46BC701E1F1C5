

class Bank_Account:
  def __init__(self):
      self. balance=0
      print("hello!!! the Deposit & withdrawl machine")

  def deposit(self):                               
    amount=float(input("enter    the amount to be deposited:"))
    self.balance+=amount 
    print("/n Amount Deposited  : ", amount)

  def Withdraw(self):
    amount=float(input("enter the amount to be withdraw:"))
    if self. balance>=amount:
       self. balance-=amount
       print("/n You Withdraw:    ",amount)
    else:
      print("/n Insufficient    balance ")
      
  def display(self):
    print("/n Account              balance =", self. balance)

# Driver code

# create an object of class
s = Bank_Account()

# call the function with that class object
s. deposit()
s. Withdraw()
s. display ()