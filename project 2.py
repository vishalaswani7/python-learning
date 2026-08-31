#STUDENT GRADE MANAGER (EACH STUDENT SHOULD HAVE 1 NAME, 2 SUBJECT, 3 MARKS)
student =[]
while True:
    print("==WELCOME TO STUDENT GRADE MANAGER==")
    print("1. add student ")
    print("2. view all student")
    print("3. calculate class average")
    pt =int(input("select option"))
#(1) add student:
    if pt == 1:
        students ={"name" : input("entre name of the student"),
                  "subject" : input("entre subject of the student"),
                  "marks" : int(input("entre marks of the student"))}
        student.append(students)
        print("==student profile added successfully==")
#(2) view all student:
    if pt ==2:
        if len(student)==0:
            print("students are not recorded yet")
        else:
         print("====list of students====")
        v = 1
        for student1 in student:
         print(f"student no. { v } -> {student1["name"]}, {student1["subject"]}, {student1["marks"]}")
         v = v+1
#class average:
    if pt == 3:
       if len(student)==0:
          print("students are not recorded yet!")
       else:
            total = 0
            for student1 in student:
              total = total + student1["marks"] 
            average = total / len(student)
            print("class average = ",average) 
    else:
       print("===THANKS FOR USING OUR SYSTEM===") 
       break       