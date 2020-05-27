import random

total = 100
print("Your Total is $" + str(total))
print("************")

#Write your game of chance functions here
def coin_flip(bet, guess, total):
  if bet <= 0:
    print("You must bet more than $0")
    return 0
  if bet > total:
    print("You don't have enough money to make that bet!")
    return 0
  print("Coin Flip!")
  print("You have bet $" + str(bet) + " and guessed " + str(guess) + ".")
  print()
  print("--------------------------------------------")
  print()

#coin_flip(5, "Heads") CODE WORKS TO THIS Point


  result = random.randint(1, 2)
  if result == 1:
    print("The coin landed on Heads!")
  elif result == 2:
    print("The coin landed on Tails!")
#coin_flip(5, "Heads") CODE WORKS TO THIS Point


  if (guess == "Heads" and result == 1):
    print("You win $" + str(bet) + "!")
    print("--------------------------------------------")
    print()
    return +bet
  elif guess == "Heads" and not result == 1:
    print("You lose $" + str(bet) + "!")
    print("--------------------------------------------")
    print()
    return -bet
  elif guess == "Tails" and result == 2:
    print("You win $" + str(bet) + "!")
    print("--------------------------------------------")
    print()
    return +bet
  elif guess == "Tails" and not result == 2:
    print("You lose $" + str(bet) + "!")
    print("--------------------------------------------")
    print()
    return -bet

def cho_han(odd_even, bet, total):
  if bet <= 0:
    print("You must bet more than $0")
    return 0
  if bet > total:
    print("You don't have enough money to make that bet!")
    return 0
  print("CHO_HAN!")
  print("You have bet $" + str(bet) + " and guessed " + str(odd_even) + ".")
  print()
  print("--------------------------------------------")
  print()

  result = random.randint(2, 12)
  if result == 2 or result == 4 or result == 6 or result == 8 or result == 10 or result == 12:
    print("The dice add up to " + str(result) + "!")
    print("Even!")
    print()
  else:
    print("The dice add up to " + str(result) + "!")
    print("Odd!")
    print()

  if (odd_even == "Even" and (result == 2 or result == 4 or result == 6 or result == 8 or result == 10 or result == 12)):
    print("You win $" + str(bet))
    return +bet
  if (odd_even == "Odd" and (result == 3 or result == 5 or result == 7 or result == 9 or result == 11)):
    print("You win $" + str(bet))
    return +bet
  else:
    print("You lose $" + str(bet))
    return -bet


#Call your game of chance functions here

total += coin_flip(5, "Heads", total)
print("Your New Total is: $" + str(total))
print("************")

total += cho_han("Odd", 5, total)
print("Your New Total is: $" + str(total))
print("************")
#total += coin_flip(5, "Heads", total)
#print("Your New Total is: $" + str(total))
#print("************")
#total += coin_flip(0, "Heads", total)
#print("Your New Total is: $" + str(total))
#print("************")
#total += coin_flip(1000, "Heads", total)
#print("Your New Total is: $" + str(total))
#print("************")
