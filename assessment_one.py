
# count

mylist = ["apple", "bananna", "blueberries", "apple"]
count = mylist.count("apple")
print(count)
print("___________")

# using enumerate and count
mylist = ["apple", "bananna", "blueberries"]

for count, item in enumerate(mylist):
    print(count, item)
print("___________")

# ord() takes a single parameter and returns ch - a unicode character

character = "P"
unicode_char = ord(character)
print("the unicode char is: ")
print(unicode_char)
print("_________________")

print("the unicode char is:")
print(ord('A'))
print("_________________")

# char() gets the character that returns the unicode

x = chr(97)
print("the character that returns the unicode:")
print(x)
print("_________________")
# append
students = [ 'lucy', 'kate', 'ellie' ]

# append() add items to the end of a list

student_name = input('what is the name of the new student?')
students.append(student_name)
print(students)
print("_________________")

# extend adds all the elements to the end of a list
year_10_students = [ 'lucy', 'kate', 'ellie' ]
year_11_students = [ 'mary', 'jane']

year_10_students.extend(year_11_students)
print('Student list using extend():',year_10_students)
print("_________________")

# how to add a new key value pair to a dict need to use append() - find the
# find the key which need to append to like title, address and age
my_family = {"Title":[],"Address":[],"Age":[]};
my_family ["Title"].append("Mum")
my_family ["Address"].append("Chester")
my_family ["Age"].append(64)
print(my_family)
print("_________________")

# count capital letters in a file

with open("text.txt") as file:
    count = 0
    text = file.read()
    for i in text:
        if i.isupper():
            count +=1
    print("Total caps in text file are ", count)
print("_________________")


# count capital letters in a string

name = str(input("Enter the sentence with cap letters: "))
count = 0
for i in name:
    if i.isupper():
        count=count+1
print("The number of capital letters found in the string is:",count)
print("_________________")

# reverse a string
reverse = "Apple"[::-1]
print(reverse)
print("_________________")

# reverse a string using a function
def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)
print("_________________")

# reverse a string using a function again
def my_function(new):
  return new[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)
print("_________________")

# SIMPLE CALULATOR
# can perform basic arithmetic operations +, - , * , /
# depending on user input
# first go at calultator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)
print("_________________")

# second go at calulator
num1 = float(input("Enter a number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter another number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator")
print("_________________")

# third go at calulator using functions - using recources

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("____Another attemp___")

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = int(input("Select operations form 1., 2.,3.,4. :"))

if choice == 1:
    print(num1, "+" , num2, "=",
          add(num1, num2))
    print("_________________")

elif choice == 2:
    print(num1, "-" , num2, "=",
          subtract(num1, num2))
    print("_________________")

elif choice == 3:
    print(num1, "*" , num2, "=",
          multiply(num1, num2))
    print("_________________")

elif choice == 4:
    print(num1, "/" , num2, "=",
         divide(num1, num2))
    print("_________________")

else:
    print("invaild input")

# BONUS READING
# iterating with four loops

# count
index = 0
values = [ 1 , 3 , 5, 6 ]

for value in values:
    print(index, value)
    index += 1
print("___end__count___")

# iterating without count
# use RANGE() with LEN() to create an index autmatically
# don't need to remember to update the index like this index += 1
# in this set value to = item in values at current value of index

values = [ 1 , 3 , 5, 6 ]

for index in range(len(values)):
    value = values[index]
    print(index, value)
print("___end__range and len___")

# in this can also forget to update the value - value =value[index]
# this wouldn't update the values column

# enumerate() - can use in same way
# gives you back two loop variables count and value
# do not need to remember to access the item or advance the index


for count, value in enumerate(values):
     print(count, value)
print("___end enumerate___")

# can change the start value of count

for count, value in enumerate(values, start=1):
     print(count, value)
print("___end enumerate start changed___")

# need to use enumerate() when need to use the count and an item in a loop
# enumerate increments the count by 1 in every iteration
name_list = ["bob","mary","jane", "janet","jackie","craig", "harry"]

for index, value in enumerate(name_list):
    print(index, value)

print("___another enumerate example___")

mydict = {
    'name': 'black tshirt',
    'size': 'small',
    'type' : 'crewneck',
    'price': 24,
    'stock': 95
}

for x in mydict:
    print(x)
print("_______prints the keys______")

for index, (key, value) in enumerate(mydict.items()):
    print(index, key, value)
print("______counter of looping through____")

