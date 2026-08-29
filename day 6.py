#LOOPS IN PYTHON
#in python loops are used to repeat a block of code multiple times.
#they help perform tasks like printing a massage several times, iterating over lists, or generating patterns
#example:-
print("hello")
print("hello")
print("hello")
#instead of writing this three times we can use loop
# there are two types of loop in python
# (1) WHILE LOOP:- a while loop runs as long as a condition is true
#syntax:-
#while Condition:
    #code to repeat
#example:-
number = 1
while number<= 3:
    print("banana")
    number = number+1
#how while loop works:-
#(1) number = 1 -> starts the number at 1
#(2) while number<= 3 -> checks weather the number is 3 or less
#(3) print("banana") -> prints banana
#(4) number = number+1 -> increases the number by 1 each time
#(5) when the number becomes 4, the while number<=3 condition becomes false so the loop stops
#practice question 1: write a program that to print numbers from 1 to 10 using a while loop
n = 1
while n<= 10:
    print(n)
    n = n+1
#practice question 2: write a program to print numbers from 10 down to 1 using a while loop
i = 10
while i>= 1:
   print(i)
   i = i-1
#practice question 3: write a program to print all even numbers between 1 and 50 using a while loop (hint: use the modulus operator % to check for even numbers.)
even_number = 1
while even_number <=50:
    if even_number % 2==0:
     print(even_number)
    even_number = even_number+1
#practice question 4: write a program that prints the sum of first n natural number. for example, if n = 5, than output should be 1 +2 +3 +4 +5 = 15(keep the running total inside the loop)
n = int(input("entre a number:"))
sum = 0
while n>=1:
   sum = sum + n
   n = n-1
print("sum =", sum)
print("n =", n)
#practice question 5: ⁠Write a program to print this pattern using a while loop:
# *
# **
# ***
# ****
q = 1
while q <= 4:
   print("*" * q)
   q = q+1
#practice question 6: vishal wants to print his name 5 times, but each time with a number in front of it
v = 1
while v<=5:
   print(v,"vishal")
   v =v+1
#practice question 7: write a program to print the multiplication table of any number using loop
t = int(input("entre numbe:"))
f = 1
while f<= 10:
   print(f"{t} x {f} = {t*f}")
   f = f+1
# (2) FOR LOOP:- for loop is used to iterate(go through) sequences like list, tuple, or strings
#syntax:- 
# for element in sequence:
             #code block
#example:-
foodlist = ["biryani", "pizza", "pasta"]
for element in foodlist:
   print(element) #output:- biryani, pizza, pasta
fruitlist = ("banana", "mango", "grapes")
for list in fruitlist:
   print(list) #output:- banana, mango
#for loop with range():- the range function generates a sequence of numbers. it is often used with loops
#syntax:- range(start, stop, step)
#start -> beginning number(default = 0)
#stop -> end limit(excluded)
#step -> increment value(default = 1)
#example:-
for item in range(1, 7, 1):
   print(item) #output:- 1, 2, 3, 4, 5, 6
#practice question 8: write a program using for and range to print all even numbers between 1 and 20
for j in range(1,21,1):
   if j % 2==0:
    print(j)
#practice question 9: Write a program to print numbers from 1 to 50, but print "vishal" instead of numbers that are multiples of 5.
l = 1
while l <= 50:
   if l %5==0:
      print("vishal")
   else:
      print(l)
   l = l+1
#practice question 10: Write a program to print the square of each number from 1 to 10 using a for loop.
for m in range(1, 11, 1):
   print(m * m)
# Write a program that prints the multiplication table of any number entered by the user using a for loop
qy = int(input("entre a number"))
for tm in range(1, 11, 1):
   print(f"{qy} x {tm} = {qy * tm} ")
#Saumya wants to print her username five times in uppercase letters Write a program to print
for gk in range(1, 6, 1):
      print("SAUMYA")
#BREAK, CONTINUE, AND PASS
#break statement: stop the loop immediately when it is encountered.
#example:-
for num in range(1, 10):
   if num == 5:
      break
   print(num) #output: 1, 2, 3, 4 (loop stops when num==5)
#continue statement:- the continue statement skips the current iteration and moves to the next one.
#example:-
for num in range(1, 6):
   if num == 3:
      continue
   print(num) #output: 1, 2, 4, 5 (3 is skipped)
#practice question 11: Write a program that prints numbers 1 to 10, but skips the number 7 using the continue statement.
for num in range(1, 11):
   if num == 7:
      continue
   print(num)
#pass statement:- the pass statement dose nothing it's used as placeholder when you want to keep a block empty
#example:-
age = 18
if age >= 18:
   pass
#here, when the condition is true, python simply dose nothing
# another example:- 
for i in range(5):
   pass
#the loop runs 5 times, but pass perform no action ( pass = "Do nothing for now")
#mini project 1: count down timer(with 1-second gap) before something "exciting" happens (like "launching...." or "happy new year!")
import time
count = int(input("entre count down number"))
print("\n count down starts now")
for i in range (count, 0 , -1):
   print(i)
   time.sleep(1)
print("\n HAPPY NEW YEAR!")
#practice question 12: Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
   print(i)
#practice question 13: Print numbers from 10 to 1 using a while loop.
beta = 10
while beta>=1:
   print(beta)
   beta = beta -1
#practice question 14: Print all numbers between 1 and 50 except multiples of 5.
for num in range(1, 51):
   if num % 5==0:
      continue
   else:
      print(num)
#practice question 15: Print the sum of first 10 natural numbers using a while loop.
lmk= 1
sumk = 0
while lmk<=10:
   sumk = sumk+ lmk
   lmk = lmk+1
print("sum =", sumk)