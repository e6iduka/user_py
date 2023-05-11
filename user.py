class User:
    def __init__(self, name):
        self.username = name
        self.money = 0
    
    def make_deposit(self, amount):
        self.money += amount
    
    def make_withdrawl(self, amount):
        if amount > self.money:
            print("You don't have enough money!")
            self.display_user_balance()
            return

        self.money -= amount

    def display_user_balance(self):
        print(f"{self.username}'s Balance: {self.money}")
    
    def transfer_money(self, other_user, amount):
        if amount > self.money:
            print("You don't have enough money!")
            self.display_user_balance()
            return
        
        self.money -= amount
        other_user.money += amount
        print(f"{self.username} has given {other_user.username} {amount} credit")


howard = User("Egi")
sadie = User("Endi")
morley = User("Klea")

# Balance is initially at zero
howard.display_user_balance()

howard.make_deposit(200)
howard.make_deposit(1000)
howard.make_deposit(700)

# Test case in case of attempt to withdraw too much
howard.make_withdrawl(2000)

# Balance should be 1900 currently.
howard.make_withdrawl(1500)
# Balance should be 400
howard.display_user_balance()


sadie.make_deposit(1234)
sadie.make_deposit(4321)
sadie.make_withdrawl(201)
sadie.make_withdrawl(1000)
# Balance should be 4354
sadie.display_user_balance()


morley.make_deposit(5000)
morley.make_deposit(1000)
morley.make_withdrawl(3000)
morley.make_withdrawl(3000)
# Balance should be 0
morley.display_user_balance()


howard.transfer_money(sadie, 200)
howard.display_user_balance()
sadie.display_user_balance()
