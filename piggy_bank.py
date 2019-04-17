#Piggy Bank Software

class bank():
    def __init__(self):
        self.balance=0
        
    def add(self):
        amount = float(input("\nAdd amount: "))
        self.balance += amount
        print("\nAfter adding , your updated balance is {} rupees".format(self.balance))
        print("None\n")
        
    def withdraw(self):
        amount = float(input("\nwithdrawing amount: "))
        self.balance -= amount
        print("\nAfter withdrawing , updated balance is {} rupees".format(self.balance))
        print("None\n")
        
    def check(self):
        print("\nYour current balance is {} rupees".format(self.balance))
        print("None\n")
    
    def start_application(self):
        app=input("Start or End:")
        while app == 'Start':
            act=input("Add, Withdraw or Check:")
            if act=='Add':
                self.add()
            elif act=='Withdraw':
                self.withdraw()
            elif act=='Check':
                self.check()
            else:
                print("Please enter correct commend!")
            app=input("Start or End:") 

saving_bank=bank()
saving_bank.start_application()