import os 
clear = lambda: os.system("cls")
clear()


user_input = input("please enter a number  : ")
user_input_list = list(user_input)


sum = 0

if int(user_input) > 0:
    for i in user_input_list:
        sum += (int(i)** len(user_input))
    if sum == int(user_input):
        print(sum, "is a Armstrong number")
    else:
        print(user_input, "is not a Armstrong number")
elif int(user_input) < 0:
    print("Please enter a positive number ")









