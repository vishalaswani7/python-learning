# MANAGEMENT SYSTEM🔥
# idea: create one program containing:-
# (1) student section
# (2) expense section
# (3) task section
# (4) exit

student_id = []
expense_id = []
task_id = []

while True:
    print("(1) student section")
    print("(2) expense section")
    print("(3) task section")
    print("(4) exit")

    a = int(input("enter your option: "))

    if a < 1 or a > 4:
        print("option not available")

    # student section:-
    if a == 1:
        print("(a) add student")
        print("(b) view students")
        print("(c) calculate average")

        b = input("enter your option: ")

        if b == "a":
            student = {
                "name": input("enter name of student: "),
                "class": input("enter class of student: "),
                "marks": int(input("enter marks of student: "))
            }
            print("student added successfully :)")
            student_id.append(student)

        elif b == "b":
            if len(student_id) == 0:
                print("no student has been added yet")
            else:
                for studentlist in student_id:
                    print(studentlist)

        elif b == "c":
            if len(student_id) == 0:
                print("no student has been added yet")
                print("average = 0")
            else:
                avg = 0
                for average in student_id:
                    avg = avg + average["marks"]

                print("average =", avg / len(student_id))

        else:
            print("option not available")

    # expense section:-
    if a == 2:
        print("(a) add expense")
        print("(b) view added expense")
        print("(c) view total spending")

        c = input("enter your option: ")

        if c == "a":
            expense = {
                "amount": int(input("enter the amount of expense: ")),
                "date": input("enter the date of expense: "),
                "type": input("enter the type of expense: ")
            }
            print("expense added successfully :)")
            expense_id.append(expense)

        elif c == "b":
            if len(expense_id) == 0:
                print("no expense has been added yet :)")
            else:
                for abc in expense_id:
                    print("=== EXPENSE ===")
                    print(abc)

        elif c == "c":
            if len(expense_id) == 0:
                print("no expense has been added yet :)")
            else:
                tot_exp = 0

                for xyz in expense_id:
                    tot_exp = tot_exp + xyz["amount"]

                print("total spending =", tot_exp)

        else:
            print("option not available")

    # task section:-
    if a == 3:
        print("(a) add task")
        print("(b) view all task")

        d = input("enter your option: ")

        if d == "a":
            task = {
                "mission": input("enter your task: "),
                "date": input("enter the date of task: ")
            }
            print("task added successfully :)")
            task_id.append(task)

        elif d == "b":
            if len(task_id) == 0:
                print("no task has been added yet :)")
            else:
                for lmn in task_id:
                    print("=== TASK ===")
                    print(lmn)

        else:
            print("option not available")

    # exit
    if a == 4:
        print("== thanks for using MANAGEMENT SYSTEM :) ==")
        break