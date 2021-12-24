from random import randint

print("""
-------------------------------
  Welcome to Guess the Number! 
       Have fun playing.            
-------------------------------
""")


def select_difficulty():
    choice = True
    while choice == True:
        mode = input("""
Please select a game difficulty:

Easy - 3 Guesses, Number to guess between 0-10
Medium - 3 Guesses, Number to guess between 0-25
Hard - 3 Guesses, Number to guess between 0-50
Custom - *Your choice* guesses, Number to guess 0-*your choice*
(You can type the full name e.g "medium" or just the first letter e.g "m") """)

        if mode.lower() == "easy" or mode.lower() == "e":
            print("You have selected Easy. Good luck and have fun!")
            choice = False
            return "easy"
        elif mode.lower() == "medium" or mode.lower() == "m":
            print("You have selected Medium. Good luck and have fun!")
            choice = False
            return "medium"
        elif mode.lower() == "hard" or mode.lower() == "h":
            print("You have selected Hard. Good luck and have fun!")
            choice = False
            return "hard"
        elif mode.lower() == "custom" or mode.lower() == "c":
            return "custom"
        else:
            continue

def game():
    num_of_guesses = 3
    current_guess = 0
    win = False

    difficulty = select_difficulty()
    if difficulty == "easy":
        num_to_guess = randint(0, 10)
        high = 10
    elif difficulty == "medium":
        num_to_guess = randint(0, 25)
        high = 25
    elif difficulty == "hard":
        num_to_guess = randint(0, 50)
        high = 50
    elif difficulty == "custom":
        num_of_guesses = int(input("How many guesses would you like? - "))
        high = int(input("Select the highest number to guess? (0, *your input*) - "))
        num_to_guess = randint(0, high)
    
    print("You have {} guesses. Good luck!".format(num_of_guesses))
    while win == False and current_guess < num_of_guesses:
        while True:
            try:
                guess = int(input("What is your guess? - "))
                if 0 <= guess <= high:
                    break
                else:
                    print("Please select a number between 0 and {}".format(high))
                    continue
            except ValueError:
                print("Please make sure to enter a number.")
                continue
        
        current_guess += 1
        if guess == num_to_guess:
            win = True
            print("You guessed correctly!")

        else:
            if guess < num_to_guess:
                print("Too low.")
            elif guess > num_to_guess:
                print("Too high.")
            if num_of_guesses - current_guess == 0:
                pass
            elif num_of_guesses - current_guess == 1:
                print("You have 1 guess left.") 
            else:
                print("You have {} guesses remaining.".format(num_of_guesses - current_guess))
            
    if win == False:
        print("Unlucky. You'll get it next time!")

    play_again = input("""
Do you want to play again? """)
    if play_again.lower() == "yes" or play_again.lower() == "y":
        game()
    else:
        print("""
------------------------
  Thanks for playing!
       Goodbye :)
------------------------
""")
game()