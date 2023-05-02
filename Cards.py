import random


def win():
  pa = input("Play again?: ").lower()
  if pa == "yes" or pa == "ye" or pa == "yeah" or pa == "yea" or pa == "yes sir" or pa == "sure" or pa == "y":
    game()
  else:
    quit()


def game():
  a = False
  Card = str(random.randint(1, 13))
  
  if Card == "1":
    Card="ace"
  
  elif Card == "11":
    Card="jester"

  elif Card == "12":
    Card="queen"

  elif Card == "13":
    Card="king"
  

  while a == False:
    asw = input("Pick A Card, Ace 2 3 4 5 6 7 8 9 10 Jester, Queen, King \n\n").lower()

    if asw == Card:
      print("Correct ")
      win()

    else:
      print("Wrong Card\n")


game()
win()
