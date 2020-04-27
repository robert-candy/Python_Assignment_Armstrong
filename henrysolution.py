
print("Presss 'q' for quit.")
while True:
    number = input("Enter a positive Number:").strip().lower()
    numberofdigits = len(number)
    summ = 0
    if number == "q":
        print("See you...")
        break
    else:
        if number.isnumeric():
            for i in range(numberofdigits):
                summ += int(number[i]) ** numberofdigits
            if summ == int(number):
                print(number, "is a Amstrong Number.")
            else:
                print(number, "is not a Amstrong Number.")
        elif number.count(".") == 1 and number.replace(".", "1").isnumeric() or number.count(",") == 1 \
                and number.replace(",", "1").isnumeric():
            print("Please enter a integer number.")
        elif number.count("-") == 1 and number.index("-") == 0 and number.replace("-", "1").isnumeric():
            print("Please enter a positive number")
        else:
            print("Do not use any entries other than numeric values")
