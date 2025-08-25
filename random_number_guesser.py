from random import randint
Is_looping = True
num = randint(1, 100)
guess = 0
guess_count = 0
print(num)

while(Is_looping):
    guess_count += 1
    try:
        guess_string = input("Guess my number from 1 to 100: ")
        guess = int(guess_string)
    except(ValueError):
        print(f"Really -_- this is not a number --> {guess_string}")
        print("Guess again\n")
    except(KeyboardInterrupt):
        print("\nFORCE QUITTING")
        Is_looping = False
    else:
        if guess == num:
            print(f"\nWell done you guessed my number in {guess_count} tries!")
            print("Game over!")
            Is_looping = False       
        elif(guess > num):
            print("\nnuh-uh, too high guess again :)\n")
            
        elif(guess < num):
            print("\nnuh-uh, too low guess again :)\n")
            

        