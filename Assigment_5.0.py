#Importing math because of the usage of math.trunc.
#Lopping the if and else statement in case the user inputs a non-number character, it can also pass through a special case when going to the except statement.
#math.trunc so the rounding off will be a normal round-off since round() function in python is not accurate to the normal round off we do in our daily lives:
#The round(_) function only rounds to the nearest even integer when the decimal point is at ".5"
#Inputting numbers not in the range of 65-100 will take you back to the inputting of grade percentage
import math
valid = True
while valid:
    try:
        gradePercent = float(input("What is your grade percentage? "))
        gradePercentage = math.trunc(gradePercent + .5)
        if 100 >= gradePercentage >= 97:
            print("Grade/Mark: 1.0")
            print("Description: Execellent")
            break
        elif 96 >= gradePercentage >= 94:
            print("Grade/Mark: 1.75")
            print("Description: Excellent")
            break
        elif 93 >= gradePercentage >= 91:
            print("Grade/Mark: 1.5")
            print("Description: Very Good")
            break
        elif 90 >= gradePercentage >= 88:
            print("Grade/Mark: 1.75")
            print("Description: Very Good")
            break
        elif 87 >= gradePercentage >= 85:
            print("Grade/Mark: 2.0")
            print("Description: Good")
            break
        elif 84 >= gradePercentage >= 82:
            print("Grade/Mark: 2.25")
            print("Description: Good")
            break
        elif 81 >= gradePercentage >= 79:
            print("Grade/Mark: 2.5")
            print("Description: Satisfactory")
            break
        elif 78 >= gradePercentage >= 76:
            print("Grade/Mark: 2.75")
            print("Description: Satisfactory")
            break
        elif gradePercentage == 75:
            print("Grade/Mark: 3.0")
            print("Description: Passing")
            break
        elif 74 >= gradePercentage >= 65:
            print("Grade/Mark: 5.0")
            print("Description: Failure")
            break
        else:
            print("Please input grade percentage from 65 - 100")
#Here we have the special cases in case the user doesn't actually have a grade in the school.
#Using .upper() so that the letters strings that will be inputted won't be case sensitivee.
#In case you put non-number characters and you aren't even included in the incomplete, withdrawn, or dropped:
#You are going back to the inquiry of grade percentage.
    except:
        status = input("Are you incomplete, withdrawn or dropped? Type YES or NO: ").upper()
        if status == "YES":
            status1 = input("What is your school status? Incomplete, withdrawn or dropped? ").upper()
            if status1 == "INCOMPLETE":
                print("Grade/Mark: Inc.")
                print("Description: Incomplete")
                exit()
            elif status1 == "WITHDRAWN":
                print("Grade/Mark: W")
                print("Description: Withdrawn")
                exit()
            elif status1 == "DROPPED":
                print("Grade/Mark: D")
                print("Description: Dropped")
                exit()
            else:
                print("Please follow the instructions properly.")
                valid = True
        else:
            print("Please input a proper grade percentage")
