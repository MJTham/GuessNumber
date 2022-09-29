#Number Guessing Game Objectives:
from art import logo
from random import *
# Include an ASCII art logo.

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def game_init():
  print(logo)
  print(f"Welcome to the Number Guessing Game!")
  print(f"I'm thinking of a number between 1 and 100.")

number = 0
def random_number():
  number = randint(1,100)
  #print(f"the answer is: {number}")
  return number

def game_level():
  difficulty_level = input("Choose the difficulty level. Type \"easy\" or \"hard\":  ").lower()
  
  if difficulty_level == "easy":
    life = 10
  else:
    life = 5

  print(f"you have {life} attempts remaining to guess the game.")
  return life

def guess_start(number,life):
  #print(f"number is {number}, and then your life is {life}")
  wrong_guess = True
  while wrong_guess:
    for _ in range(life - 1, -1, -1):
      guess = int(input("Make a guess: "))
      
      if guess == number:
        print(f"You Won!")
        wrong_guess = False
        break
      elif guess > number:
        print(f"too high")
      elif guess < number:
        print(f"too low")
  
      print(f"Guess again.")
      
      print(f"You have {_} attempts remaining to guess the number.")

      if _ == 0:
        print("You lose")
        wrong_guess = False
        
game_init()
correct_answer = random_number()
game = game_level()
guess_start(number = correct_answer, life = game)
