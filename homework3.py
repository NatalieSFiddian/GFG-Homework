# Task 1
"""
Create a program that tells you whether or not you need an umbrella
when you leave the house.
The program should:
1. Ask you if it is raining using input()
2. If the input is 'y', it should output 'Take an umbrella'
3. If the input is 'n', it should output 'You don't need an umbrella
"""

rain = input("Is it raining? y/n  ")

if rain == "y":
    print("Take an umbrella")

else:
    print("You don't need an umbrella")
print("____________________")
# Redo task one

rain = input("Is it raining? (y/n)  ")


if rain == "y":
    umbrella = input("Do you have an umbrella? (y/n) ")
    if umbrella == "y":
        print("You need to take that umbrella with you")
    else:
        print("Good luck you are going to get wet")
elif rain != "y" and rain != "n":
    print("This is invalid")
else:
    print("You don't need an umbrella")
print("____________________")
"""
Question 2
I'm on holiday and want to hire a boat. The boat hire costs £20 + a 
refundable £5 deposit. I've written a program to check that I can afford 
the cost, but something doesn't seem right. Have a look at my program 
and work out what I've done wrong
"""

my_money = input('How much money do you have? ')
boat_cost = 20 + 5

if int(my_money) > int(boat_cost):
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')
print("____________________")
""" 
Your friend works for an antique book shop that sells books between 
1800 and 1950 and wants to quickly categorise books by the century 
and decade that they were written. Write a program that takes a year 
(e.g. 1872) and outputs the century and decade (e.g. "Eighteenth 
Century, Seventies")
"""
number = int(input("Enter the year between 1800 and 1950:"))

decades = ["0's", "10's", "20's", "30's","40's", "50", "60's", "70's", "80's", "90's"]

if number < 1800 or number > 1950:
    print("Please enter the number between 1800 and 1950")

else:
    temp = number

# returns the decade which is a modulo operator
# how many times the right num makes up the left num (not the answer) the remainding number is the answer
# a = 1802
# b = 100
# answer = a % 100
# print(answer)

decade = temp % 100
print("Decade =", decade)

# returns the century of the dividing temp by 100
century = int(temp/100)
print("Century =", century)

myAnswer = ""

if century == 19:
    myAnswer = "Twenteenth Century, "

else:
    myAnswer = "Nineteenth Century, "

#
indices = int(decade/10)
print("Indices =",indices)

myAnswer += decades[indices]
print("MyAnswer =", myAnswer)

print(myAnswer)
print("____________________")
"""
I'm setting up my own market stall to sell chocolates. I need a basic till 
to check the prices of different chocolates that I sell. I've started the 
program and included the chocolates and their prices. Finish the 
program by asking the user to input an item and then output its price.
"""

""" 
This is a dictionary – they use key:value pairs to hold and retreive data. Keys are 
unique and are made up of strings or ints while values are made up of anything. 
You retreive a value (in this case the price) if we know its key – which will be the 

"""

chocolates = {
'white': 1.50,
'milk': 1.20,
'dark': 1.80,
'vegan': 2.00,
}

choice = input("Enter a chocolate: ")

if 'white' in choice:
    print("The price of white chocolate is:", chocolates.get('white'))
elif 'milk' in choice:
    print("The price of milk chocolate is:", chocolates.get('milk'))
elif 'dark' in choice:
    print("The price of dark chocolate is:", chocolates.get('dark'))
else:
    print("The price of vegan chocolate is:", chocolates.get('vegan'))

print("____________________")

# Question 3
"""
Write a program that simulates a lottery. The program should have a 
list of seven numbers that represent a lottery ticket. It should then 
generate seven random numbers. After comparing the two sets of 
numbers, the program should output a prize based on the number of 
matches:

"""

# lottery one attempt
import random

lottery_ticket = [2, 18, 56, 97, 23, 19 , 5]
print("Your ticket numbers are...")
print(sorted(lottery_ticket))

lottery_draw = list(range(1, 100))
random.shuffle(lottery_draw)

seven_nums = lottery_draw[:7]
print("The lottery draw numbers are....")
print(sorted(seven_nums))

print("The matching numbers are ...")
print("__________________")

# lottery second attempt
import random

# Initialise an empty list that will be used to store the 7 numbers
lottery_numbers = []

lottery_ticket = [12, 18, 56, 97, 23, 19, 32]
print("Your ticket numbers are...")
print(sorted(lottery_ticket))

for i in range(0, 7):
    number = random.randint(1, 100)
    # Check if this number has already been picked and ...
    while number in lottery_numbers:
        # ... if it has, pick a new number instead
        number = random.randint(1, 100)
    # Now that we have a unique number, let's append it to our list.
    lottery_numbers.append(number)

# Sort the list in ascending order
lottery_numbers.sort()

# Display the list on screen:
print(" Today's lottery numbers are... ")
print(lottery_numbers)

# Display matching numbers
# using list comprehension and enumerate() + len()
# Matching elements count
matching = len([num for num, value in enumerate(lottery_numbers) if value in set(lottery_ticket)])

if matching == 3:
    print("Total matching numbers are", matching)
    print("You win £20")

elif matching == 4:
    print("Total matching numbers are", matching)
    print("You win £40")

elif matching == 5:
    print("Total matching numbers are", matching)
    print("You win £100")

elif matching == 6:
    print("Total matching numbers are", matching)
    print("You win £1000")

elif matching == 7:
    print("Total matching numbers are", matching)
    print("You win £100000")

else:
    print("You have no matching numbers")
print("____________________")

# TASK 3
# Question 2

"""
This program should save my data to a file, but it doesn't work when I 
run it. What is the problem and how do I fix it?
 
poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'r') as poem_file:
poem_file.write(poem)

 The problem with this is it said r – for read file instead of w – for write file 

"""

myfile = open("poem.text", 'w')
myfile.write("I like Python and I am not very good at poems")
myfile.close()

"""
Question 3
Here is a snippet of Elton John’s song “I’m Still Standing”
"""
lyrics = [
    "\nYou could never know what it's like",
    "\nYour blood like winter freezes just like ice",
    "\nAnd there's a cold lonely light that shines from you",
    "\nYou'll wind up like the wreck you hide behind that mask you use",
 
    "\nAnd did you think this fool could never win?",
    "\nWell look at me, I'm coming back again",
    "\nI got a taste of love in a simple way",
    "\nAnd if you need to know while I'm still standing, you just fade away",
 
    "\nDon't you know I'm still standing better than I ever did",
    "\nLooking like a true survivor, feeling like a little kid",
    "\nI'm still standing after all this time",
    "\nPicking up the pieces of my life without you on my mind",
 
    "\nI'm still standing (Yeah, yeah, yeah)",
    "\nI'm still standing (Yeah, yeah, yeah)",
]

myfile = open("poem.text", 'w')
myfile.write(lyrics)
myfile.close()
print("__________________")


lyrics = [

    "\nYou could never know what it's like",
    "\nYour blood like winter freezes just like ice",
    "\nAnd there's a cold lonely light that shines from you",
    "\nYou'll wind up like the wreck you hide behind that mask you use",

    "\nAnd did you think this fool could never win?",
    "\nWell look at me, I'm coming back again",
    "\nI got a taste of love in a simple way",
    "\nAnd if you need to know while I'm still standing, you just fade away",

    "\nDon't you know I'm still standing better than I ever did",
    "\nLooking like a true survivor, feeling like a little kid",
    "\nI'm still standing after all this time",
    "\nPicking up the pieces of my life without you on my mind",

    "\nI'm still standing (Yeah, yeah, yeah)",
    "\nI'm still standing (Yeah, yeah, yeah)",
]

myfile = open("poem.text", 'w')
myfile.writelines(lyrics)
myfile.close()
print("__________________")

for line in lyrics:
    if 'still' in line:
        print("The lines that have still in them: ")
        print(line)

