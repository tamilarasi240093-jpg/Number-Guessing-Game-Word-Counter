print("hi")
import random


def guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    score = 100

    print("\n=== Number Guessing Game ===")
    print("Guess a number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            score = max(100 - (attempts - 1) * 10, 10)
            print("Correct! You won!")
            print("Attempts:", attempts)
            print("Your Score:", score)
            break
        elif guess < number:
            print("Too Low! Try again.")
        else:
            print("Too High! Try again.")

guessing_game()
from collections import Counter
import string

def word_counter():
    print("\n=== Word Counter ===")

    try:
        with open("sample.txt", "r") as file:
            text = file.read().lower()

        words = text.translate(
            str.maketrans("", "", string.punctuation)
        ).split()

        frequency = Counter(words)

        print("Total Words:", len(words))
        print("\nMost Common Words:")

        for word, count in frequency.most_common(5):
            print(word, ":", count)

    except FileNotFoundError:
        print("File not found!")

word_counter()