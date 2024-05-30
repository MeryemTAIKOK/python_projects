import random
computer_number = random.randrange(9)
try:
    number = input("Guess number!! ==>")
except ValueError:
    print("Why did you feed me an error?")
except Exception as e:
    # Custom message for any other exception
    print("An error occurred:", e)

if type(number) == str:
    print("Why did you feed me a String")
    exit

user_number = int(number)

if user_number < computer_number:
    print("you're number is less than what I think")
elif user_number > computer_number:
    print("you're number is bigger than what I think")
    

