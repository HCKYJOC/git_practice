import random

money = 100

#Write your game of chance functions here
def coin_flip(bet, guess):
  result = random.randint(1, 2)
  if result == 1:
    return "Heads!"
  elif result == 2:
    return "Tails!"
  if (guess == "Heads" and result == "Heads!"):
    money += bet
    print(str(result) + " You win " + str(bet) + "!")
    print("New Total: " + str(money))
    return money
  elif guess == "Heads" and not result == "Heads!":
    money -= bet
    print(str(result) + " You lose " + str(bet) + "!")
    print("New Total: " + str(money))
    return money
  elif guess == "Tails" and result == "Tails!":
    money += bet
    print(str(result) + " You win " + str(bet) + "!")
    print("New Total: " + str(money))
    return money
  elif guess == "Tails" and not result == "Tails!":
    money -= bet
    print(str(result) + " You lose " + str(bet) + "!")
    print("New Total: " + str(money))
    return money

#Call your game of chance functions here
print(coin_flip(5, "Heads"))
