# # Calculator for floats
# N1 = float(input("First: "))
# N2 = float(input("Second: "))
# sum = N1 + N2
# print("sum " + str(sum))
#
# # String manipulation
# course = "Python for beginners"
# copy = course[-4:]
# print(copy)
# # Concatenation
# first = "John "
# last = "Smith"
# message = first + last + ' is a coder '
# print(message)
# course = 'python for beginners'
# # Length function
# print(len(course))
# # Replace function - returns original string if given string does not exist
# print(course.replace("burn", "mojiz"))
# # In function
# print("pyhon" in course)
#
# # Math import
# import math
#
# # Floor function, Ceiling function
# x = 2.3
# print(math.floor(x))
# # Abs function
# x = -2.9
# print(abs(x))
#
# # If - elif - else
# is_hot = False
# is_cold = False
# if is_hot:
#     # to enter ' in a string, use " for the string and vice versa
#     print("it's a hot day")
#     print("enjoy your day")
# elif is_cold:
#     print("it's a cold day than wear warm clothes")
# else:
#     print("it's a lovely day")
#
# # Logical operators
# good_credit = False
# price = 1000000
# if good_credit:
#     print(price * 0.1)
# else:
#     print(price * 0.2)
# has_good_credit = False
# has_good_income = True
# has_criminal_record = False
# if has_good_income and not has_good_credit and not has_criminal_record:
#     print("not eligible for loan")
# has_good_credit = True
# has_good_income = False
# has_criminal_record = False
# if has_good_income or has_good_credit and not has_criminal_record:
#     print("eligible for loan")
# has_good_income = True
# has_criminal_record = False
# if has_good_income and not has_criminal_record:
#     print("eligible for loan")
#
# # if condition
# temperature = 30
# if temperature > 30:
#     print("It's a hot day")
#
# # string length validation
# name = "mmhhhhh"
# if len(name) < (3):
#     print("name must be atleast 3 chareters")
# elif len(name) > (50):
#     print("name can be maximum of 50 charecters")
# else:
#     print(name + " looks good")
#
# # weight units converter
# N1 = float(input("weight: "))
# N2 = input("(K)gs or (L)bs:")
# # to compare input in lowercase and uppercase both, we convert to upper() and compare or to lower() and compare
# if N2.lower() == "k":
#     print(str(N1 * 2.20462) + " pounds")
# if N2.upper() == "L":
#     print(str(N1 / 2.20462) + " kilos")
# #kilos
# #
# guess_number = 0
# answer_found = False
# while guess_number <= 2:
#     questionString = "Guess number " + str(guess_number + 1) + " : "
#     moj = input(questionString)
#     if int(moj) == 9:
#         answer_found = True
#         print("You won")
#         break
#
#     guess_number = guess_number + 1
# if not answer_found:
#     print("You lose")
#
# # Guess = 9
# # input("Guess:")
# # if Guess == 9:
# #     print("You win")
# # while Guess: <= int(3):
# #     Guess = Guess + 1
# # print("sorry you failed")
#
#
# N1 = float(input("First: "))
# The_Question = input("what operator do you want to use (-,+,*,/): ")
# while The_Question is not ("-" or "+" or "/" or "*"):
#     The_Question = input("invalid input try something else: ")
# N2 = float(input("Second: "))
# if The_Question == "+":
#     print(N1 + N2)
# elif The_Question == "-":
#     print(N1 - N2)
# elif The_Question == "*":
#     print(N1 * N2)
# elif The_Question == "/":
#     if N2 == 0:
#         print("invalid input")
#     else:
#         print(N1 / N2)
# else:
#     print("invalid input")
# input("thank you for using this product. How do you think we can improve it ? ")
# print("your response was helpful byeee")
#
#
# while True:
#     N1 = float(input("temperature: "))
#     N2 = input("(C)elsius or (F)ahrenheit:")
#     # to compare input in lowercase and uppercase both, we convert to upper() and compare or to lower() and compare
#     if N2.lower() == "c":
#         print(str((N1 * 9/5) + 32) + " Fahreinheit")
#     if N2.lower() == "f":
#         print(str((N1 - 32) * 5 / 9) + " degrees celsius")
#     p = input("do you want to exit the program ? y or n ")
#     if p.upper() == 'Y':
#         input("thank you for using this product. How do you think we can improve it ? ")
#         print("your response was helpful byeee")
#         break
#
#
#
# car_running = False
# while True:
#     mp = input(">")
#     if mp.lower() == "help":
#         print('''start - to start the car
# stop - to stop the car
# quit - to exit''')
#     elif mp == "start":
#         car_running = True
#         print("Car started...Ready to go!")
#     elif mp == "stop":
#         if car_running:
#             car_running = False
#             print("car stopped.")
#         else:
#             print("car was not running, cannot be stopped")
#     elif mp == "quit":
#         break
#     else:
#         print("I don't understand that...")
#         # continue while
#
# for item in range(5, 10, 2):
#     print(item)

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")
#
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y}) ')
#
numbers = [5, 2, 5, 2, 2, 0, 2, 2, 2, 2, 2, 0, 5, 2, 5, 2, 5]
for x in numbers:
    for i in range(x):
        print("x", end="")
    print("")