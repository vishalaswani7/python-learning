#DICTIONARY IN PYTHON: a dictionary is in built data type in python used to store data in KEY-VALUE PAIRS
#each key is unique and maps to a value
#example of dictionary:-
student = {"name" : "vishal",
           "age" : 18,
           "city" : "delhi"}
#here: "name", "age", "city"-> keys
#dictionary mutable(can be changed) and dose not allow duplicate keys
#in dictionary you can access values using key not index because dictionary is key based not index based
#list -> position/index -> fruit[o]
#dictionary -> key -> student["name"]
print(type(student)) #output <class 'dict'>
print(student["name"]) #output vishal
print(student["age"]) #output 18
print(student["city"]) #output delhi
#if we create a key of a same name multiple times, the last occurrence of that key and its value will overwrite any previous occurrences
# if you assign the same key again -> old value gets replaced
#example:
fruit = {"fruit 1": "banana",
         "fruit 2": "lichee",
         "fruit 3": "pineapple",
         "fruit 1": "grapes"} 
print(fruit) #output: "grapes", "lichee", "pineapple". grapes will overwrite banana
#ADDING OR UPDATING VALUES: you can add new key-value pair or modify the existing once:-
student["roll number"] = 31 #adds new key-value pair
print(student) #output: vishal, 18, delhi,31
student["age"] = 19 #modify the existing key value convenient for single key
print(student) #output: vishal, 19, delhi, 31
#we can also remove the existing key with .pop(" ")
student.pop("roll number")
print(student) #output: vishal, 19, delhi -> "roll number" key got removed
#DICTIONARY METHOD:-
# (1) .keys() returns all key 
print(student.keys()) #output: "name", "age", "city"
# (2) .values() returns all the values
print(student.values()) #output: vishal, 19, delhi
# (3) .items() return all key-values pairs as tuples
print(student.items()) #output: ([('name', 'vishal'), ('age', 19), ('city', 'delhi')])
# (4) .get("key") returns value of a key safely
print(student.get("name")) #output: vishal
# (5) .update(new-dict) updates dictionary with another its convenient for multiple key
student.update({"city": "pune",
                "age": 20})
print(student)
#practice question 1: create a dictionary named marks to store marks of 3 subjects. add the subject one by one and print the final dictionary
marks = {"1st subject marks": input("entre first subject marks"),
         "2nd subject marks": input("entre second subject marks"),
         "3rd subject marks": input("entre third subject marks")}
print(marks)
#SETS IN PYTHON:- a set is a collection of unrecorded and unique items. 
#set automatically removes duplicate elements and are written under curly braces{ }
language = {"python", "c++", "java", "python"}
print(language) #output: python, c++, java 
#set methods:-
# (1) .add(" ") adds element
language.add("advance js")
print(language) #output: python, c++, java, advance js
# (2) .remove(" ") removes element
language.remove("advance js")
print(language) #output: python, c++, java
# (3) .pop removes a random element
language.pop()
print(language) #output: any 2 element out of 3
# (4) .union(set2) combine sets without duplicate
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2)) #output: 1, 2, 3, 4, 5, 6
# (5) .intersection(set2) gives element that are common on both set
print(set1.intersection(set2))
# (6) .clear() empties the set
set1.clear()
print(set1) #output: set1() it clears the element of a set
#TYPE CONVERSION: we can also convert list or tuple into set and can also convert set into list or set.
number_list= [1, 2, 3, 4] #type -> list
#to convert this into set :-
number_set = set(number_list) #list -> set
print(type(number_set)) #output -> set
number_list = list(number_set) #set -> list
print(type(number_list)) #output: list
number_tuple = tuple(number_list) #list -> tuple
print(type(number_tuple)) #output: tuple
# practice number 2: You are given a list of programming languages ["Python", "Java", "C++", "Python", "advance js"] Convert it into a set and print how many unique languages Divya knows
languageslist = ["python", "java", "c++", " advance js"]
print(type(languageslist)) #output: list
languagesset = set(languageslist)
print(type(languagesset)) #output: set 
print(len(languagesset)) #output: 4
#mini assignment:-
# (1) create a dictionary storing total marks of maths, chemistry, bio subject as input and print them
marks_of_student = {"maths" : int(input("entre the marks of maths")),
                    "chemistry" : int(input("entre the marks of chemistry")),
                    "bio" : int(input("entre the marks of bio"))}
print(marks_of_student)
# (2) create a set of numbers and show union and intersection with other set
set3 = {1, 2, 3, 4, 5}
set4 = {3, 4, 5, 6, 7}
print(set3.union(set4)) #output 1, 2, 3, 4, 5, 6, 7
print(set3.intersection(set4)) #output 3, 4, 5