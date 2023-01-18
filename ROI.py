
class ROICalculator:
    def __init__(self):
        self.user_ri = 0
        self.user_expenses = 0
        

    def income(self):
        x = input("What is your rental income? : ")
        user_q = input("Any other misc income? ('yes or no'): ")
        if user_q.lower() == "yes":
            user_misc = input("How much misc income? : ")
            # user_ri = int(user_misc) + int(x)
            print(f"Your rental income is: {x}")
        elif user_q.lower() == "no": 
            print(f"Your rental income is: {x}")
        self.user_ri = int(user_misc) + int(x)

    def expenses(self):
        user_tax = input("What are your tax expenses? : ")
        user_insur = input("What are your insurance expenses? :")      
        user_exp = input("Any other expenses? ('yes or no'): ")
        if user_exp.lower() == "yes":
            other_exp = input("How much more combined expenses? : ")
            self.user_expenses = int(user_tax)+int(user_insur)+int(other_exp)
            print(f"Your total expenses are: {self.user_expenses}")
        elif user_exp.lower() == "no":
            self.user_expenses = int(user_tax)+int(user_insur)
            print(f"Your total expenses are: {self.user_expenses}")
        

    def cash_flow(self):
        cash =  self.user_ri - self.user_expenses
        print(f"Your cash flow is: {cash}")

    def run(self):
        question = input("Need to use the ROI calculator? ('yes' or 'no'): ")
        if question.lower() == "yes":
            self.income()
            self.expenses()
            self.cash_flow()
        elif question.lower() == "no":
            print("Okay goodbye")
        

b = ROICalculator()
ROICalculator.run(b)

