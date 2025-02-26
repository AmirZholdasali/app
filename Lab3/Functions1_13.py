import random
random_number = random.randint(1, 20)
name = input("Hello! What is your name?\n")
print(f"Well, {name}, I am thinking of a number between 1 and 20.\ntake a guess")
attempts = 0
guess = random_number+1
while guess != random_number:
    guess = int(input())
    if guess < random_number:
        attempts += 1
        print("Your guess is too low.\nTake a guess.")
    if guess > random_number:
        attempts += 1
        print("Your guess is too high.\nTake a guess.")
    
if guess == random_number:
    print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
