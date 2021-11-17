valid = True
while valid:
    try:
        print("This program will determine the lowest number on the three numbers you will be inputting.")
        firstNumber = float(input("Enter 1st number: "))
        secondNumber = float(input("Enter 2nd number: "))
        thirdNumber = float(input("Enter 3rd number: "))
        if firstNumber <= secondNumber and firstNumber <= thirdNumber:
            print(firstNumber)
        elif secondNumber <= firstNumber and secondNumber <= thirdNumber:
            print(secondNumber)
        elif thirdNumber <= firstNumber and thirdNumber <= secondNumber:
            print(thirdNumber)
        break
    except:
         print("Input a valid number")

