#INTRODUCTION TO FUNCTIONS
#A function in python is a block of reusable code that performs a specific task. instead of writing the same line repeatedly, we define a function once and use it multiple times
#Example:- without function
print("hello")
print("hello")
print("hello")
#Example;- with function
def greet():
    print("hello")
greet() #function calling
greet()
greet()
#USING FUNCTION IS USEFUL BECAUSE:-
#(1)reusability: write the code once -> use it many times
#(2)less code: instead of repeating 20 lines you can just call function
#(3)easy fix: you wrote the same 10-20 line, you can call one function
#practice question 1: write a function named welcome_massager() that prints "welcome to python programming!" three times.
def welcome_massager():
    print("welcome to python programming!")
welcome_massager()
welcome_massager()
welcome_massager()
#practice question 2: define a function inspire() that prints a motivational quote with your name.
def inspire():
    print("having a great power and not using it to your advantage is something only a fool would do! \n VISHAL")
inspire()
#practice question 3: explain what happens if you call a function before defining it:
# we will get error because we need to define a function before calling it
#function parameters and argument:
#function can accept parameter, data passed from outside. the values given when calling the function are arguments.
def greet(name):
    print("hello", name)
greet("saumya singh")
def add(a, b):
    print("sum=", a+b)
add(5, 10) #output 15
#parameters:- A parameter is a variable written inside the parameter when you define aa function
# def greet(name):
#here, name is parameter.
#arguments:- A argument is the actual value you give to the function when you call it.
#greet("vishal")
#here, "vishal" is argument.
#python put "vishal" argument into name parameter so,
def greet(name): #name -> parameter
    print(name)
greet("vishal") #"vishal" -> argument
#default argument:- if no argument is provided, a default value is used.
def greet(name = "vishal"):
    print("hello", name)
greet() #output -> hello vishal(default value)
greet("saumya") #output -> hello saumya
#default parameter = a value that is automatically used when no argument is provided.
#it is useful because they make parameter optional. if no argument is provided , python uses the default value instead of giving an error
#return statement:-
#a return statement sends a value from a function back to the place where the function was called
def add(a, b):
    return a + b
result = add(10, 20)
print("result=", result)
#variable scope:-
#(1)local variable:- a variable created inside a function is usually a local variable
#example
def greet():
   name = "vishal"
   print(name)
greet()
#here, name belongs to the greet() function
#you cannot normally use it out side the function
#(2)global variable:- a variable created outside the function is global variable
name ="vishal"
def greet():
    print(name)
greet() #output vishal the function can access the global variable because it was created outside.
# none in python:-
# A special value in python that represent the absence of a value, a function that doesn't explicitly return a value returns none:-
def greet():
    print("hello")
result =greet()
print(result)
#output:-
#hello
#none
#why did none appear?
#because the function didn't return anything
#python automatically return none when a function reaches the end without a return value.