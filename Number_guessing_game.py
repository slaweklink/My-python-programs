# This is a number guessing game.
import random

print("Provide a low range for me:")
low_range = int(input())

print("Provide a high range:")
high_range = int(input())

number = random.randint(low_range,high_range)
print(number)

# let's start the guessing game
print("Try to guess my number")
user_number = int(input())
while user_number != number:
    try: 
        if user_number > number:
            print("Your number is too high")
            user_number = int(input())
        if user_number < number:
            print("Your number is too low")
            user_number = int(input())
    except ValueError:
        print("That's not a number")

print("You guessed correctly, it's ", user_number) 