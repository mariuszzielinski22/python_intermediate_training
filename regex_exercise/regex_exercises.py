import re


def exercise_1():
    print('Write number here:')
    value = input()

    expression = "[0-9]+"
    if re.fullmatch(expression, value):
        print("Found number")
        if int(value) % 2 == 0:
            print("Even Number")
        else:
            print("Number is odd")
    else:
        print("Incorect Input")


def exercise_2():
    print("Write postal code here:")
    value = input()

    expression = "[0-9]{2}-[0-9]{3}"
    if re.fullmatch(expression, value):
        print("Postal code is correct")
    else:
        print("Postal code is incorrect, type in xx-xxx")
