#Number Guessing Game Objectives:
from art import logo
from random import randint
# Include an ASCII art logo.

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game_level():
  difficulty_level = input("Choose the difficulty level. Type \"easy\" or \"hard\":  ").lower()
  
  if difficulty_level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def guess_start(guess,number,life):
  if guess > number:
    print(f"too high")
    return life - 1
  elif guess < number:
    print(f"too low")
    return life - 1
  else:
    print(f"You Won!")
  

def game_init():
  print(logo)
  print(f"Welcome to the Number Guessing Game!")
  print(f"I'm thinking of a number between 1 and 100.")
  number = randint(1, 100)
  
  game = game_level()
  guess = 0
  while guess != number:
    print(f"you have {game} attempts remaining to guess the game.")
  
    guess = int(input("Make a guess: "))

    game = guess_start(guess, number, game)
    if game == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != number:
        print("Guess again.")
        
game_init()
