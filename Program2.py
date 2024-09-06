# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
# Multiple Input
#name = input("What is your name? ")
#name = input("What is your name? ")
#
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)



## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.
name = input("What is your name? ")
print(name)
print(name)



## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.
name = input("What is your name? ")
print("!" + name + "!" + name + "!")

## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630
first=input("Tell me your name first name: ")
last=input("Tell me your last name: ")
street_adress=input("what is your street adress: ")
city=input("what us your city and postal code: ")
print("First Name: "+first)
print("Last Name:"+last)
print("street adress: "+ street_adress)
print("city and postal code: "+city)
## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out
one= input("Give me one word: ")
two= input("give me another word: ")
three= input("Give me the last word: ")
print(one + "-" + two + "-" + three)
## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.
name=input("Tyoe in a name: ")
year=input("Tpye in a year: ")
print("The year was " + year + " and there was a dangerous dog named " + name + " outside of the house.")
print(name + " The dog was still outside of my house for a long time, after an 1 hour the pet control came.")