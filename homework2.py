# TASK 3 Q1
# correct this code to run

chairs = '15'
nails = 4
total_nails = int(chairs) * nails
message = 'I need to buy {} nails'.format(total_nails)
print(message)

# TASK 3 Q2
# correct this code to run

my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make. Write a program to
# calculate this.
# Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be able to easily
# change these values if I want. The output should say something like:
# You can make 9 omelettes with 6 boxes of eggs

boxes = input("How many boxes of eggs do you have? ")
# this logic is going to tell me the how many eggs are in the total boxes
# by * 6 and then divide this by 4 because 4 eggs make an omlette
omelettes = int(boxes) * 6 / 4
print(" You can make {} omlettes with {} boxes of eggs".format(omelettes, boxes))

# formatting string tasks
# Task 1 - Replace the (.) character with (!) instead. Output should be “I love coding!”
my_str = "I love coding."
my_str = my_str.replace(".", "!")
print(my_str)

# Task 2 - Reassign str so that all of its characters are lowercase.
my_str_1 = "EVERY Exercise Brings Me Closer to Completing my GOALS."
my_str_1 = my_str_1.lower()
print(my_str_1)

# Task 3 - Output whether this string starts with an A or not
my_str_2 = "We enjoy travelling"
ans_1 = my_str_2.startswith("A")
print(ans_1)

# Task4 - What is the length of the given string?
my_str_3 = "1.458.001"
ans_2 = len(my_str_3)
print(ans_2)

#  Complete a series of tasks to slice strings

# Task 1 - Slice the word so that you get "thon".
wrd = "Python"
print(wrd[2:6])

# Task 2 - Slice the word until "o". (Pyth)
wrd = "Python"
print(wrd[0:4])

# Task 3 - Now try to get "th" only.
wrd = "Python"
# Type your answer here.
print(wrd[2:4])

# Task 4 - Now slice the word with steps of 2, excluding first and last characters
wrd = "Python"
# Type your answer here.
print(wrd[2:-1:2])

# Explain what this program does:

for number in range(100):
    output = 'o' * number
    print(output)

""" 
The range function generates a sequence of numbers starting from the given 
start int to the stop int
the for loop with range() repeats the action of added an 'o' * the number in range()
"""
'''
Your boss really likes calculating VAT on their purchases. It is their favourite hobby. They've written this code to
calculate VAT and need your help to fix it.

When your boss runs the program they get the following output:
None 
Your boss expects the program to output the value 120 . What is wrong? How do you fix it?
'''


def calculate_vat(amount):
    return amount * 1.2


print("The VAT calculated is ", (calculate_vat(100)))

""" 
Write a new function to print a ‘cashier receipt’ output for a shop (any shop – clothes, food, events etc).
It should accept 3 items, then sum them up and print out a detailed receipt with TOTAL.

For example:
Input:
Item_1_name = ‘Trainers’
Item_1_price = 50.45
Item_2_name = ‘T-shirt
Item_2_price = 12

Output:
Trainers 50.45
T-shirt 12.00

TOTAL        62.45
"""

# Praticing
# shopping list pratice

shopping_list = {'Nike hoodie': 75, 'Addidas T-shirt': 42, 'Trek trainers': 75, 'Reebok shorts': 17}


def print_cashier_receipt(products):
    sum_total = (sum(products.values()))
    # print(sum_total) this is the total the value of the dictionary element
    for key, value in products.items():
        print(key, '', '£', value)  # Print the key-value pair in new line

    print("Shopping List Total: ", "£", sum_total)  # print the total of the value.


print_cashier_receipt(shopping_list)  # call the function


# Practicing
# shopping list practice with user input

shopping_list = []
list_length = 3

for idx in range(list_length):
    item = input('Enter item to buy: ')
    shopping_list.append(item)

print(shopping_list)

# Practicing
# shopping list practice with user input and condictions

shopping_list = []

max_length = 4

while len(shopping_list) < max_length:
    item = input('Enter item you want to buy: ')
    if item not in shopping_list:
        shopping_list.append(item)
    elif item == item:
        print("Duplicate item - will not be added to list")
print(shopping_list)

# Practicing
# shopping list pratice

