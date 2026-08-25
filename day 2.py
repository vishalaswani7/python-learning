#  TYPES OF DATA
#string: sequence of characters
food = "pasta" 
print("my favorite food is :" , food)
# integer: whole number positive or negative 
age = 18
print("my age is : " , age)
#float: numbers with decimals
x = 14.5 
print("the value of x is:" , x)
#bool: logical values like true or false 
question4 = True 
print("the answer of question4 is :" , question4)
# use type() function to check a variable data type
print(type(food))
print(type(age))
print(type(x))
print(type(question4))
#key words in python: keywords are special words in python that holds special meaning and it cannot be used as variable name
#list of key words: and, continue, except, global, lambada, pass, while, as, def, assert, del, finally, import, nonlocal, return, yield, break, elif, for, in, not, true, class, else, from, is, or, try
#tip: use help("keywords") in python shell to list all current keywords
#practice : try to create a variable with keyword and see what error you get
# got syntax error : invalid syntax 
# assignment1: print sum program input two numbers and print their sum
number1 = int(input("entre first number"))
number2 = int(input("entre second number"))
print("the total of first and second number is :" , number1 + number2)
#assignment2: modify the sum program to find the average of two numbers instead of the sum
number1 = int(input("entre first number"))
number2 = int(input("entre second number"))
print("the average is :" , (number1 + number2) / 2)
#type conversions: type conversion means changing the data type from one type to another 
#types of conversion : (A) implicit conversion (automatic) python converts smaller data to larger once automatically to prevent data loss. Example:
# x = 5 : int
# y = 2.5 : float
# z = x + y : python converts int to float
# print(z) : output 7.5
#                      (B) explicit conversion(manual) manual convert data type using in-built functions. Example:
# x = 5 : int
# y = float(x) : converts int to float data type 
#common functions : int(), float(), str(), bool()
#assignment3 : take a number as input, convert it to a float, and print both the original and converted values with their data types
x = 15
y = float(x)
print("the value before conversion was :" , x)
print("the value after conversion is :" , y)
print("the data type before conversion was :" , type(x))
print("the data type after conversion is :" , type(y))
#types of operators in python :
# 1 arithmetic operators : used for mathematical calculations. Example: +, -, *  etc
x = 10
y = x + 5
print("thr value of y is :" , y) #output : the value of y is : 15
# 2 comparison operator : used to compare values. Example ==, !=, >, <  etc
x = 10
y = 15
print(y > x) #output : true
a = 20
b = 30
print( b < a) #output : false
# 3 logical operators : used for logical operations (true/false)
print(x < y and b > a) #output : true
print(x < y and b < a) #output : false
print(y < x and a > b) #output : false
# 4 assignment operator : use to assign values to variable. Example: =, += -=, *=  etc
a = 10 # a = 10
a+= 10 # a = a + 10
a-= 10 # a = a - 10
# assignment5 : write a program that takes two numbers and prints their sum, difference, and product and weather the first number is greater than the second
firstnumber =int(input("entre first number"))
secondnumber =int(input("entre second number"))
print("the sum of two numbers is :" , firstnumber + secondnumber)
print("the difference between the first and second number is:" , firstnumber - secondnumber)
print("the first number is greater" , firstnumber > secondnumber)