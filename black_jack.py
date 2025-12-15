import random               
# Generate a random number. 
GENERATED_NUMBER = random.randint(1,100)
print(GENERATED_NUMBER)



decision = input("Enter your prefered mode:easy or hard ").lower()

chance = 10

def guessTheNumber(num, mode):
    global chance
    print(num)

    def game_type(input):
        if input == "easy":
            global chance
            chance=10
            return "easy"
        else:
            chance = 8
            return "hard"
    
    game_mode = game_type(mode)
    if mode == game_mode:
        chance = chance
        while chance > 0:
            guess = int(input("Enter your guess"))
            print("Your guess: ", guess)
            if num > guess:
                print("Too low, guess a higher number")
                chance -=1
                print(f"You have {chance} left")
                # guess = int(input("Enter your guess"))
            elif num < guess:
                print("Too high, guess a lower number")
                chance -=1
                print(f"You have {chance} left")
                # guess = int(input("Enter your guess"))
            elif num == guess:
                print("Great, you guessed it right.")
                chance = 0
            else:
                print("Enter a valid input")
                chance -=1
    print(f"The right number was {num}")


guessTheNumber(GENERATED_NUMBER,decision)
# make the user elect between modes. easy or hard.
# if easy then 10 turns, if had then 8 turns. 
# then make user guess number. if higher then provided number then print "Too high."
#  If lower then provided number thn print("Too low").
#  If user gusses within 10 or 8 guess then user wins, else user loose.
