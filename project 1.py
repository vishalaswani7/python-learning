#MINI PROJECT :- EXPENSE TRACKER
#question/problem statement: create a console based-based expense tracker program in python that allows the user to recorded daily expenses and view summaries like total spending. use only the concepts learned till chapter 6(loops, condition, list, dictionaries, and basic input/output)
#project details / description:
#You are required to build a simple personal finance management tool. The program should allow the user to:
#(1) Add an expense with details like date, category, description, and amount.
#(2) View all recorded expenses in a clean format.
#(3) calculate total spending so far.
#(4) Exit the program gracefully when the user chooses to.
#All tasks must be implemented using loops, if-else, lists, and dictionaries only. No user-defined functions or file handling should be used.
expenses = [] #list of all expenses in form of dictionary
print("WELCOME TO EXPENSE TRACKER")
while True:
    print("===MENU===")
    print("1. add expense")
    print("2. view all expense")
    print("3. view total expense")
    print("4. Exit")
    choice = int(input("entre your choice"))
#add expense
    if choice == 1:
       date = input("entre date of expense")
       category = input("entre type of expense(example: food, party, etc...)")
       amount = float(input("entre the amount"))
       expense= {"date" : date,
                 "category" : category,
                 "amount" : amount}
       expenses.append(expense)
       print("expense is added successfully")
#view all expenses
    elif choice == 2:
        if(len(expenses)==0):
            print("no expenses added yet")
        else:
            print("===expenses===")
            count = 1
            for kharcha in expenses:
                print(f"expense no. {count} -> {kharcha["date"]},{kharcha["category"]}, {kharcha["amount"]}")
                count = count+1
#view total spending
    elif choice == 3:
        total= 0
        for kharcha in expenses:
            total = total+ kharcha["amount"]
        print("total spending = ", total)
# exit
    else :
        print(" thankyou for using our system")
        break