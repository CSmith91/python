import random

# init the game
top_of_range = input("Type a number greater than 0: ")

try:
    # Attempt to convert the input to an integer
    top_of_range = int(top_of_range)
    
    # Ensure the input number is positive
    if top_of_range <= 0:
        print("You needed to type a positive number.")
        quit()

except ValueError:
    # If conversion to int fails, handle the error
    print("You didn't type a number.")
    quit()

# create our random number and a guess counter
random_number = random.randint(0, top_of_range)
guesses = 0

# use a while loop (with a break) to continually ask the user to guess the number
while True:
    guesses +=1
    user_guess = input("Make a guess: ")

    try:
        user_guess = int(user_guess)

    except ValueError:
        # If conversion to int fails, handle the error
        print("You didn't type a number.")
        # brings us back to the top of the loop
        continue

    # if user gets the exact value, we can break the while loop and inform the user, otherwise we inform the user if their guess was too high or too low
    if user_guess == random_number:
        print("You got it! It took you", guesses, "guesses")
        break
    elif user_guess > random_number:
        print("Try lower")
    else:
        print("Try higher")
