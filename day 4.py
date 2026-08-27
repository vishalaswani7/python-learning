# CONDITIONAL STATEMENT IN PYTHON
# conditional statement allows your program to make decisions-run different parts of code based on certain condition
# what are condition?
# condition are simple statement that can either be true or false. Example:
age = 18
print(age>= 18)
# if statement : use to run a block of code only when the condition is true
age = int(input("entre your age "))
if age >= 18:
    print("you are eligible to vote")
# if the statement is false, Nothing happens.
# else statement: used when python wants to execute a block of code when the condition is false. Example:
age = int(input("entre your age")) #if age = 17
if age >= 18:
    print("you are an adult")
else:
    print("you are not an adult") #output
#practice question 1: write a python program that takes a numbers input and prints:
# "positive" if number > 0
# "zero" if number == 0
# "negative" if number < 0
number = float(input("entre number"))
if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")
#LISTS IN PYTHON: a list is in built data type that can store multiple values in a single variable.
# lists are mutable(can be change) and can store different data types.
marks = [34, 54, 65, 79]
foods = ["pizza", "burger", "cola"]
student = ["vishal", 18, "mumbai"]
print(len(foods))
print("index o of food is" , foods[0])
print("index 2 of food is", foods[2])
#MODIFYING ELEMENTS :
# (1) list are changeable:
age = [1,2,3,4]
age[0]= 5
print(age)
# (2) list slicing: you can extract parts of a list using slicing
marks = [45,64,76,87,92]
print(marks[1:3])
print(marks[-3:-1])
print(marks[:-1])
print(marks[2:])
#LIST FUNCTION:-
# (1) len(list) returns length of list
print(len(marks)) #output 5
# (2) max(list) returns largest value
print(max(marks)) # output 92
# (3) min(list) returns smallest value
print(min(marks)) # output 45
#LIST METHOD:- Methods you can use to add, remove, sort, and rearrange items in list
list = ["a", "b", "c"]
# (1) .append(el) add element at the end of list
list.append("d")
print(list[3]) #output d
# (2) .insert(i, x) add an item at specific index
list.insert(2, "x")
print(list) #output a b x c d
# (3) .remove(x) removes the first occurrence of an item
list.remove("x")
print(list) # a b c d
# (4) .pop(i) removes the item at specific index
list.pop(3)
print(list) #output a b c
# (5) .sort() sorts the list in ascending order
list.sort()
print(list) #output a b c
# (6) .reverse() reverses the list
list.reverse()
print(list) #output c b a
#practice question 2: write a program that takes names of 3 favorite foods from the user and stores them in a list the print the list and its length
food1 = input("entre 1st food")
food2 = input("entre 2nd food")
food3 = input("entre 3rd food")
food4 = [food1, food2, food3]
print(food4)
print(len(food4))
#TUPLES IN PYTHON : A tuple is a built in data type that stores multiple values like list but tuple is immutable(cannot be changed after created)
day = ("monday", "tuesday", "wednesday")
# difference between string and tuple: 
#list[] -> mutable
#tuple()-> immutable
#IMPORTANT: parentheses() alone dont make a string A string is written inside quotes(" ")
# A single value inside parentheses() is not automatically makes a tuple if we add comma that what makes it a tuple. Example
alphabet = ("a", "b", "c") #tuple because it has comma and parentheses together.
sunday = ("fun day",) #tuple : to make a string tuple you need comma(,)
#tuple methods:-
# (1) .count(el) counts occurrences of a value
print(alphabet.count("a")) #output 1
# (2) .index(el) return first index of element
print(alphabet.index("b")) #output 1
#practice question 3: create tuple of your 2 favorite fruit then print: the total number of fruits and the index of one selected fruit
fruit1 = input("entre 1st fruit",)
fruit2 = input("entre 2nd fruit",)
fruit3 = (fruit1, fruit2)
print(len(fruit3))
print(fruit3.index(fruit2))
#assignment 1:ask user for 3 favorite movie and store them in a list
movie1 = input("entre the name of your first movie")
movie2 = input("entre the name of your second movie")
movie3 = input("entre the name of your third movie")
movie = [movie1, movie2, movie3]
#assignment 2: create a tuple of marks and print the highest and lowest marks
mark = (45, 52, 67, 83, 95)
print(max(mark))
print(min(mark))
# assignment 3: write a program to check grade based on marks (A/B/C/D) using if-elif-else.
x = int(input("entre your marks"))
if x >= 90:
    print("A grade")
elif x >= 75:
    print("B grade")
elif x >= 50:
    print("C Grade")
else:
    print("D grade")