# imports
import time
import sys
# taking user info
name = input("What is your name? ")
print("Welcome to the world of DC WE ARE THE WIZARDS OF THE OLD " + name)
birth_year = input("what is the year you were born on: ")
# checking valid birth year
if int(birth_year) > 2023:
    sys.exit("Invalid input. Bye Bye")
if int(birth_year)<1972:
    sys.exit("sorry this time we are hoping this power will get to a newer generation")
# calculating age
age = 2023 - int(birth_year)
profession = input("What is your profession? ")
if profession == "jobless":
    sys.exit ('sorry get a job we will try again')


home = input('Where is your home? ')
if home == "homeless":
    sys.exit("sorry just don't try again")
# take a user input, but we are not doing anything with it
m = input("Why do you think yourself worthy of wielding the power of us wizards? ")

# if it is me, I am worthy
if name.upper() == "MOJIZ":
    k = "You are worthy"
    n = "You are " + str(age) + " years old you are a " + profession + " you live in " + home + " ,you were right when you said, \"" + m + "\" and you are worthy of our power, shazam!"
else:
    k = "You are unworthy "
    n = "What nonsense! You are " + str(age) + " years old, you are a " + profession + ", you live in " + home + " and the statement you gave which was " + m + " was wrong and thus you are unworthy, shazam!"

# pause before printing all info
time.sleep(1)
print("your age is " + str(age))
time.sleep(0.5)
print("you are a " + profession)
time.sleep(0.5)
print("you live in " + home)
# pause before deciding whether worthy or unworthy
time.sleep(3)
print(k)
print(n)

