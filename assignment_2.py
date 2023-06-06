#
# N1 = float(input("First: "))
# N2 = float(input("Second: "))
# The_Question = input("what operator do you want to use (-,+,*,/): ")
# while The_Question is not ("-" or "+" or "/" or "*"):
#     The_Question = input("invalid input try something else: ")
#     if "-" or "+" or "*" or "/":
#         break
# if The_Question == "+":
#     print(N1 + N2)
# elif The_Question == "-":
#     print(N1 - N2)
# elif The_Question == "*":
#     print(N1 * N2)
# elif The_Question == "/":
#     print(N1 / N2)
# else:
#     print("invalid input")
# input("thank you for using this product. How do you think we can improve it ? ")
# print("your response was helpful byeee")







N1 = float(input("First: "))
The_Question = input("what operator do you want to use (-,+,*,/): ")
while The_Question not in "-/*+":
    The_Question = input("invalid input try something else: ")
N2 = float(input("Second: "))
if The_Question == "+":
    print(N1 + N2)
elif The_Question == "-":
    print(N1 - N2)
elif The_Question == "*":
    print(N1 * N2)
elif The_Question == "/":
    if N2 == 0:
        print("invalid input")
    else:
        print(N1 / N2)
else:
    print("invalid input")
input("thank you for using this product. How do you think we can improve it ? ")
print("your response was helpful byeee")

