import random

# ASCII Art for the game banner
banner = """
  _______ _            _   _                 _               

 |__   __| |          | \ | |               | |              
    | |  | |__   ___  |  \| | _   _ _ __ ___ | |__   ___ _ __ 
    | |  | '_ \ / _ \ | . ` || | | | '_ ` _ \| '_ \ / _ \ '__|
    | |  | | | |  __/ | |\  || |_| | | | | | | |_) |  __/ |   
    |_|  |_| |_|\___| |_| \_| \__,_|_| |_| |_|_.__/ \___|_|   
"""

print(banner)
print("I'm thinking of a number between 1 and 50.")
print("Can you guess it within 6 attempts?")
print("-" * 55)

# Generate a random number between 1 and 50
secret_number = random.randint(1, 50)
attempts = 0
max_attempts = 6

# Main game loop
while attempts < max_attempts:
    guess_input = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ")
    
    # Check if the input is a valid number
    if not guess_input.isdigit():
        print("❌ Invalid input! Please enter a number.")
        continue
        
    guess = int(guess_input)
    attempts += 1
    
    # Check the guess
    if guess < secret_number:
        print("📈 Too low! Try a higher number.")
    elif guess > secret_number:
        print("📉 Too high! Try a lower number.")
    else:
        print(f"\n🎉 CONGRATULATIONS! You guessed the number in {attempts} attempts!")
        break
else:
    # This runs only if the loop finishes without hitting 'break'
    print(f"\n😢 Game Over! You've run out of attempts. The number was {secret_number}.")
