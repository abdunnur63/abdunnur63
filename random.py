import random
# Set the secret word
words = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
secret_word = random.choice(words)

guesses_remaining = 6
player_has_won = False

while guesses_remaining > 0 and not player_has_won:
    # Get the player's guess
guesses = input("Enter your guess:")

if guess == secret_word:
    player_has_won = True
else:
    print("Incrroect guess. Try again.")
guesses_remaining -=1

if player_has_won:
    print("Congratulations, you won!")
else:
    print("Sorry, you ran out of guess. The secret wprd was", secret_word)

