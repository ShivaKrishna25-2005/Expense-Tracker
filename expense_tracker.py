#expense tracer:


expenses=[]
def add_expense():
    amount=float(input("enter the user amount:"))
    expenses.append(amount)
    print("Expenses added successfully!!.\n")

def show_total_expense():
    total=sum(expenses)
    print("Total expenses are:", total ,"\n")

def highest_expense():
    if len(expenses) == 0:
        print("NO amount recorded")

    else:
        highest=max(expenses)
        print("Highest expenses are:", highest, "\n")

while True:
    print("1.Add Expenses:")
    print("2.Show Expenses:")
    print("3.Highest Expenses:")
    print("4.Exit:")

    choice=input("Enter your choice:")
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_total_expense()
    elif choice == "3":
        highest_expense()
    elif choice == "4":
        print("Invalid choice choosen!!")
        break
    else:
        exit
         
                 
