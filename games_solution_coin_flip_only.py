import random

total = 100

def coin_flip(guess, bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        return 0
        print("------------------")

    #Starts the game and flips the coin
    print("------------------")
    print("Let's flip a coin! You guessed " + guess)
    result = random.randint(1,2)

    # Prints the result of the coin flip. A 1 is heads, a 2 is tails
    if result == 1:
        print("Heads!")
    elif result == 2:
        print("Tails")

    # Determines if you won or lost and returns either bet or -bet
    if (guess == "Heads" and result == 1) or (guess == "Tails" and result == 2):
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet
    else:
        print("You lost " + str(bet)+" dollars!")
        print("------------------")
        return -bet



total += coin_flip("Heads", 10)

print("Your total amount of money is " + str(total))
