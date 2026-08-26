# assignment 1 : TEMPERATURE CONVERTER take input in celsius and print its equivalent in fahrenheit and kelvin(use explicit type conversion and arithmetic operators)
celsius = float(input("entre temperature in celsius:"))
fahrenheit = ( celsius * 9/5) + 32
kelvin = celsius + 273.15
print("temperature in celsius is :" , celsius)
print("temperature in fahrenheit is:" , fahrenheit)
print("temperature in kelvin is:" , kelvin)
# assignment 2 : BILL SPLIT CALCULATOR write a program that takes TOTAL BILL AMOUNT and NUMBER OF FRIENDS and calculate HOW MUCH EACH PERSON WILL PAY. And also print the data type of each variable used
total_bill= float(input("entre total amount of bill:"))
friends = int(input("entre the number of friends:"))
print("each friend has to pay :" , total_bill / friends)
print("the data type of total bill is" , type(total_bill))
print("the data type of friends is" , type(friends))
#strings : strings are type of data in python that is stores sequence of numbers, characters, latters, or symbol enclosed in a single(' '), double(" "), or triple(''' ''')
#example:
a = 'hello'
b = "hello"
c = '''hello'''
print(a)
print(b)
print(c)
#strings are immutable : it cannot be changed directly we cant change name = "vishal" to directly "vishal123" we have to create new string to do so.
# string concatenation : joining two or more strings together to make one string. Example:
a = "hello"
b = '''vishal'''
print(a + " " + b)
#or
print("hello" + " " + '''vishal''')
# use (" ") to crete space between strings
# LENGTH OF STRING: we use len() to find length of a string in python. Example
print(len("vishal")) #output 6
#INDEXING IN PYTHON: each and every character in a string has its position(index) starting from 0.
#Example: a = "vishal".  index: 0 1 2 3 4 5. chrs: v i s h a l
#food = "samosa"  print(str([0]) output: s,  print(str([3]) output: o
#strings are immutable: name = "vishal"  name[0] = "b"  output: error strings cannot be changed directly
#practice question 1 : write a program that takes user's name as input and prints the first character, the last character, and the total length of the name
name = input("entre your name")
print("the first character of the name is:" ,name[0])
print("the last character of the name is:" ,name[-1])
print("total length of thr name is:" ,len(name))
#SLICING : slicing lets you access a part of a string. if you want to print the first 3 characters of the name, write:
name = "vishal"
print(name[0 : 3])  #output: vis
print(name[3 : ])   #output: hal
#IMP: print(name[0 : 3]) dose not mean print(name[0], +""+ name[3]). it means start to print from 0 index and stop before 3 index
#practice question 2 : write a program that takes your favorite food name as input and prints the middle 3 characters and the last 2 characters
food = input("entre the name of your favorite food:")
middle = len(food)//2
print("the middle three character of your favorite food is:" ,food[middle-1 : middle+2])
print("the last two characters of your favorite food is :" ,food[-2:])
#COMMON STRING METHODS :
#1 .upper() converts all characters to uppercase
str = "banana"
print(str.upper()) #output: BANANA 
#2 .lower() converts all characters to lowercase
print(str.lower()) #output: banana
#3 .title() capitalizes the first latter of each word
print(str.title()) #output: Banana
#4 .find("sub") return index of first occurrence 
print(str.find("na")) #output: 2
#5 .replace("old" , "new") replace all occurrence
print(str.replace("banana" , "orange")) #output: orange
#6 .count("sub") counts occurrence
print(str.count("n")) #output 2
#practice question 3 : write a program that takes a sentence as input and converts it to lowercase and replace all spaces " " with underscore"_" and prints the new string
sentence = input("entre the sentence")
print(sentence.lower())
print(sentence.replace(" " , "_"))
print(sentence.lower().replace(" " , "_"))
#escape sequences: escape sequences let you use special formatting in strings.
#1 \n new line
print("hello \n world")
#2 \t tab space
print("A \t B")
#3 \\ backslash
print("c://newfile")
#4 \' single quote
print('it\s great')
#5 \" double quote
print("he said\"hi\"")
# PROJECT: emoji converter basic version (no if, no loop)
emoji = input("entre emoji")
print(emoji.replace(";)" , "😉"))
print(emoji.replace(":)" , "🙂"))
print(emoji.replace(":(" , "☹️"))