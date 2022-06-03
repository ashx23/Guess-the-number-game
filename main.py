import random
from art import logo
print(logo)
easy_level_turns = 10
hard_level_turns = 5

turns = 0
# Function to check user's guess.
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1   
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! the answer was {answer}.")


# Choosing the difficulty.


def set_difficulty():
    level = input("Choose the difficulty. Type 'easy' or 'hard': ")
    if level == "easy":

        return easy_level_turns
    else:
        return hard_level_turns


def game():
    # Choosing a random number between 1 and 100.
  print("Welcome to number guessing game!\n")
  print("I am thinking of a number between 1 and 100.")

  answer = random.randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Guess a number : "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of the guesses. You lose.")
      return

game()
