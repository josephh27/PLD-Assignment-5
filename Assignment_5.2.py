#Always looping until you input a proper number
#Added some varieties of printing, time travelling if you're negative years old. You are probably from the future or something.
running = True
while running:
    try:
        age = int(input("Enter your age: "))
        if 0 <= age <= 12:
            print("You are a kid")
        elif 13 <= age <= 17:
            print("You are a teen")
        elif age == 18:
            print("You are in your debut stage")
        elif 122 >= age >= 19:
            print("You are now an adult")
        elif age > 122:
            print("Congratulations! You broke the world guinness record for the oldest person to have ever lived!")
        else:
            print("You are time travelling")
        break
    except:
        print("Please input a proper number of age")