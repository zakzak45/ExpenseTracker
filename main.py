


class Expense:
    def __init__(self,expense_id,amount,description,catergory,expense_date):
        self.expense_id=expense_id;
        self.amount=amount;
        self.catergory=catergory;
        self.description=description;
        self.expense_date=expense_date;





    def display(self):
        print(f"amount : {self.amount}")
        print(f"catergory : {self.catergory}")
        print(f"description : {self.description}") 
        print(f"expense_date : {self.expense_date}")
       


class ExpenseMananger:
    def __init__(self):
        self.expenses=[]



    def addExpense(self,expense_id,amount,description,catergory,expense_date):   
        expense_id=len(self.expenses)+1
        expense=Expense(expense_id,amount,description,catergory,expense_date)
        self.expenses.append(expense)

        print("Expense has been addedd succefully")


    def listExpenses(self):
        for expense in self.expenses:
            expense.display()

mananger=ExpenseMananger()

mananger.addExpense(1,120,"expense","Food","21 Novermber")
mananger.listExpenses()

print(mananger)
