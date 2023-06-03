# Calculator for floats
N1 = float(input("First: "))
N2 = float(input("Second: "))
sum = N1 + N2
print("sum " + str(sum))

# String manipulation
course = "Python for beginners"
copy = course[-4:]
print(copy)
# Concatenation
first = "John "
last = "Smith"
message = first + last + ' is a coder '
print(message)
course = 'python for beginners'
# Length function
print(len(course))
# Replace function - returns original string if given string does not exist
print(course.replace("burn", "mojiz"))
# In function
print("pyhon" in course)

# Math import
import math

# Floor function, Ceiling function
x = 2.3
print(math.floor(x))
# Abs function
x = -2.9
print(abs(x))

# If - elif - else
is_hot = False
is_cold = False
if is_hot:
    # to enter ' in a string, use " for the string and vice versa
    print("it's a hot day")
    print("enjoy your day")
elif is_cold:
    print("it's a cold day than wear warm clothes")
else:
    print("it's a lovely day")

# Logical operators
good_credit = False
price = 1000000
if good_credit:
    print(price * 0.1)
else:
    print(price * 0.2)
has_good_credit = False
has_good_income = True
has_criminal_record = False
if has_good_income and not has_good_credit and not has_criminal_record:
    print("not eligible for loan")
has_good_credit = True
has_good_income = False
has_criminal_record = False
if has_good_income or has_good_credit and not has_criminal_record:
    print("eligible for loan")
has_good_income = True
has_criminal_record = False
if has_good_income and not has_criminal_record:
    print("eligible for loan")

# if condition
temperature = 30
if temperature > 30:
    print("It's a hot day")

# string length validation
name = "mmhhhhh"
if len(name) < (3):
    print("name must be atleast 3 chareters")
elif len(name) > (50):
    print("name can be maximum of 50 charecters")
else:
    print(name + " looks good")

# weight units converter
N1 = float(input("weight: "))
N2 = input("(K)gs or (L)bs:")
# to compare input in lowercase and uppercase both, we convert to upper() and compare or to lower() and compare
if N2.lower() == "k":
    print(str(N1 * 2.20462) + " pounds")
if N2.upper() == "L":
    print(str(N1 / 2.20462) + " kilos")

# guessing game
guess_number = 0
answer_found = False
while guess_number <= 2:
    questionString = "Guess number " + str(guess_number+1 ) + " : "
    moj = input(questionString)
    if int(moj) == 9:
        answer_found = True
        print("You win")
        break
    guess_number = guess_number + 1
if not answer_found:
    print("You lose")

# Guess = 9
# input("Guess:")
# if Guess == 9:
#     print("You win")
# while Guess: <= int(3):
#     Guess = Guess + 1
# print("sorry you failed")

