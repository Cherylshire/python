#Learning Python! This is a lot like Ruby!

# print
print("abcdefghijklmnopqrstuvwxyz")

# variable
character_name = "Harry Potter"
character_age = "20.332" #float, no "" need in Python, like Ruby
is_male = False # boolean
character_children_number = "3"
wife_name = "Ginny"

print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")
print("He has a wife name " + wife_name +" and " + character_children_number + " children.")
print("They are a very happy family.")

#string, index
print ("Giraffe\nZoo") # add new line
print ("Giraffe\"Zoo") # print literatly.
print ("Giraffe\\Zoo")

phrase = "Middle Earth"
print(phrase +" is an awesome place!")
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(phrase.len(phrase))
print(phrase[0]) #index start with 0, just like Ruby!
print(phrase.index("d"))
print(phrase.replace("Middle", "Highland"))

#number, integer
print(4)
print(7.3)
print(2 + 3.4)
print((6 + 3) * 18)
print(20 % 3)

num = 5
print(num)
print(str(num)) # integer => string

run = -5
print(pow(run)) # 5, the absolute value of a nagitive number is always positive.

print(max(1,4,8)) #maximus number
print(min(1,4,8)) #minmus number
print(round(5.3))
print(round(5.9))

from math import *

print(floor(8.3))
print(ceil(3.7))
print(sqrt(100))

# input from user
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello" + name + "! You are " + age + "!!")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result1 = float(num1) + float(num2) # result1 = int(num1) + int(num2)
result2 = float(num1) - float(num2) # result2 = int(num1) - int(num2)
result3 = float(num1) * float(num2) # result3 = int(num1) * int(num2)
result4 = float(num1) / float(num2) # result4 = int(num1) / int(num2)

print(result1)
print(result2)
print(result3)
print(result4)

#mad lib
color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
adjective = input("Enter an adjective: ")
celebrity = input("Enter a celebrity: ")


print("Roses are { color }.")
print("{ plural noun } are blue.")
print("Sunshine are { adjective }!")
print("And I love { celebrity }!!")

#list 1
friends = ["Ginny", "Dean", "Legolas", "Hermione","Samwise", "Neville", 4, True]
friends[6] = [6]
print(friends)
print(friends[0])
print(friends[1:5]) # set a range.

#list 2
lucky_numbers = [4, 8, 15, 16, 23, 28, 42]
friends = ["Ginny", "Dean", "Legolas", "Hermione","Samwise", "Neville", 6, True]
print(friends.extend(luckey_number)) #extend the list of friends
print(friends.append("Creed")) #add another element at the end of the list.
print(friends.insert(1, "Aragorn"))
print(friends.remove(True))
print(friends.pop()) #pop out the last an element.
print(friends.index("Harry")) #check to see if the list has an element call "Harry".
print(friends.count("Legolas")) #count how many time one element show up in one list
print(friends.sort()) #alphatical order, acending number
print(friends.reverse())
friends2 = friends.copy()
# print(friends.clear()) clear everything.

# Tuples
coordinates = (4, 5) # can not be changed, add, or subtract.
# coordinates[1] = 11 # Python will give error, if you try to set a tuple into another value. since tuple can not be changed. tuple object does not support item assignment.
print(coordinates[5])
coordinates_list_of_tuples = [(1, 5), (4, 8), (9, 6)]

#function
def sayhi():
  print("Hello user, how are you?")

print("Top top")
sayhi()
print("Bottom bottom")

def say_hello(name, age):
  print("Hello" + name + ", you are " age)

say_hello("Harry", "30")
say_hello("Ronald", "31")

def name_age(name, age):
  print("Hello" + name + ", you are " str(age))

name_age("Ginny", 28)
name_age("Hermione", 29)



