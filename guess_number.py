number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))
num_guesses = 3

while guess != 'q' and num_guesses > 0:
    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"You have {num_guesses} guesses left.")
        if int(guess) < number:
            print("Too low!")
        else:
            print("Too high!")
        guess = input("Try again: ")
        num_guesses -= 1

if guess == 'q':
    print(f"The number was {number}.")