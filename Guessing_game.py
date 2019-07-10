#program guesses a number from 1 to 100

ceiling = 100
floor = 1
guesses = 0
answer = " "

while answer != "y":
    guess = int((ceiling + floor)/2)
    print("Is your number %d? (y)es, it's (h)igher, it's (l)ower" %guess)
    answer = input()
    if answer == "y":
         break
    elif answer == "h":
        floor = guess
    elif answer == "l":
         ceiling = guess


