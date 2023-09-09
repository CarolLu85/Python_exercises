from art import logo
import random
print("Welcome to the YiYi's game")
print(logo)
ACTUAL_NUMBER = random.randint(1,100)
print("I'm thinking of a number between 1 and 100")
end_of_game = False

def play_game(turns):
  while turns > 0:
    guess = int(input("Please make a guess:"))
    print("guess")
    if guess > ACTUAL_NUMBER:
      print("too high, guess again")
    elif guess < ACTUAL_NUMBER:
      print("too low, guess again")
    else:
      print(f"you got the right number, the number is {ACTUAL_NUMBER}")
    turns -= 1
    print(f"You have {turns} times left")
    print(f"The number is {ACTUAL_NUMBER}")



while not end_of_game:
  game_level = input("please choose a game level, type 'easy' or 'hard'\n")
  if game_level == "easy":
    attempt = 10
  elif game_level == "hard":
    attempt = 5
  play_game(attempt)
  ask_again = input("do you want to continue? type 'Y' or 'N'").lower()
  if ask_again == "n":
    print("The End")
    end_of_game = True