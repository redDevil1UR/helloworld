while True:
    N1 = float(input("temperature: "))
    N2 = input("(C)elsius or (F)ahrenheit:")
    # to compare input in lowercase and uppercase both, we convert to upper() and compare or to lower() and compare
    if N2.lower() == "c":
        print(str((N1 * 9/5) + 32) + " Fahreinheit")
    if N2.lower() == "f":
        print(str((N1 - 32) * 5 / 9) + " degrees celsius")
    p = input("do you want to exit the program ? y or n ")
    if p.upper() == 'Y':
        input("thank you for using this product. How do you think we can improve it ? ")
        print("your response was helpful byeee")
        break



# guess_number = 0
# answer_found = False
# while guess_number <= 2:
#     questionString = "Guess number " + str(guess_number+1 ) + " : "
#     moj = input(questionString)
#     if int(moj) == 9:
#         answer_found = True
#         print("You win")
#         break
#     guess_number = guess_number + 1
# if not answer_found:
#     print("You lose")
