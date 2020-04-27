import os 
clear = lambda: os.system("cls")
clear()

while True:
    number = input("Enter a positive Number:").strip().lower()
    digits = len(number)
    summ = 0
    if number.isnumeric():
        for i in range(digits):
            summ += int(number[i]) ** digits
        if summ == int(number):
            print(number, "is a Amstrong Number.")
            break
        else:
            print(number, "is not a Amstrong Number.")
    elif number.count(".") == 1 and number.replace(".", "1").isnumeric() or number.count(",") == 1 \
            and number.replace(",", "1").isnumeric():
            print("Please enter a integer number.")
    elif number.count("-") == 1 and number.index("-") == 0 and number.replace("-", "1").isnumeric():
        print("Please enter a positive number")
    else:
        print("Do not use any entries other than numeric values")
