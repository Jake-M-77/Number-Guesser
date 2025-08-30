from random import randint
import os

def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def difficulty_setter():
    while True:

        try:

            level_setter = int(input("What difficulty level would you like (1:Easy 2:Medium 3:Hard) -> "))
        
            if level_setter == 1:
                return randint(1, 30), 30
            elif level_setter == 2:
                return randint(1, 60), 60
            elif level_setter == 3:
                return randint(1, 90), 90
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid format!")
            print("\nPlease enter 1, 2, or 3.")

def start_game():
    
    is_looping = True
    guess = 0
    guess_count = 0
    num = 0
    max_number = 0

    clear_console()
    print("🎉 Welcome to the Number Guessing Game! 🎉\n")


    try:
        num, max_number = difficulty_setter()
    except TypeError:
        print("Invalid format!")

    # Development purposes only
    #print(num)

    while is_looping:
        
        guess_count += 1

        try:
            #Can not shorten this to one line if i want to keep my funny response :(
            guess_string = input(f"Guess my number from 1 to {max_number}: ")
            guess = int(guess_string)
        except ValueError:
            print(f"Really -_- this is not a number --> {guess_string}")
            print("Guess again\n")
        except KeyboardInterrupt:
            print("\nFORCE QUITTING")
            is_looping = False
        else:
            if guess == num:
                print(f"\nWell done you guessed my number in {guess_count} tries!")
                print("Game over!")

                replay = input("Would you like to play again? (Y/N): ")
                replay = replay.upper()

                if replay == "Y":
                    clear_console()
                    num, max_number = difficulty_setter()
                    guess_count = 0
                # Development purposes only
                #    print(num)
                    continue
                else:
                    is_looping = False  
                    clear_console()
                    print("Quitting game!")    


            elif(guess > num):
                print("\nnuh-uh, too high guess again :)\n")
                
            elif(guess < num):
                print("\nnuh-uh, too low guess again :)\n")



start_game()
