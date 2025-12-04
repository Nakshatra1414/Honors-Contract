import random

# -----------------------------------------
# CONFIGURATION
# -----------------------------------------
COLORS = ["R", "G", "B", "Y", "O", "P", "W"]  
# Red, Green, Blue, Yellow, Orange, Purple, White
CODE_LENGTH = 4
MAX_ATTEMPTS = 10


# -----------------------------------------
# Generate secret code
# -----------------------------------------
def generate_secret_code():
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]


# -----------------------------------------
# Validate user's guess
# -----------------------------------------
def validate_guess(guess):
    if len(guess) != CODE_LENGTH:
        print(f"Your guess must have exactly {CODE_LENGTH} colors.")
        return False

    for c in guess:
        if c not in COLORS:
            print(f"Invalid color '{c}'. Use only: {', '.join(COLORS)}")
            return False
    return True


# -----------------------------------------
# Evaluate guess -> returns (correct_pos, correct_color)
# correct_pos = correct color & correct position
# correct_color = correct color but wrong position
# -----------------------------------------
def evaluate_guess(secret, guess):
    secret_copy = secret[:]   # temp since we'll modify it
    guess_copy = guess[:]

    # First pass: correct positions
    correct_pos = 0
    for i in range(CODE_LENGTH):
        if guess_copy[i] == secret_copy[i]:
            correct_pos += 1
            # Mark them so they are not reused
            secret_copy[i] = None
            guess_copy[i] = None

    # Second pass: correct color, wrong position
    correct_color = 0
    for i in range(CODE_LENGTH):
        if guess_copy[i] is not None and guess_copy[i] in secret_copy:
            correct_color += 1
            # Remove matched color so it isn't reused
            secret_copy[secret_copy.index(guess_copy[i])] = None

    return correct_pos, correct_color


# -----------------------------------------
# Main Game Loop
# -----------------------------------------
def play_mastermind():
    print("\n🎮 Welcome to Mastermind!")
    print("Available colors:", ", ".join(COLORS))
    print(f"Enter your guess as {CODE_LENGTH} letters (e.g., RGBY)")
    print(f"You have {MAX_ATTEMPTS} attempts.\n")

    secret = generate_secret_code()
    # print("DEBUG SECRET:", secret)   # <-- uncomment for testing

    attempts = 0

    while attempts < MAX_ATTEMPTS:
        raw_guess = input(f"Attempt {attempts + 1}: ").upper()
        guess = list(raw_guess)

        if not validate_guess(guess):
            continue

        attempts += 1
        correct_pos, correct_color = evaluate_guess(secret, guess)

        if correct_pos == CODE_LENGTH:
            print("\n🎉 Congratulations! You broke the code!")
            print("Secret code was:", " ".join(secret))
            return

        print(f"⚪ Correct Color + Correct Position: {correct_pos}")
        print(f"🔵 Correct Color (Wrong Position): {correct_color}\n")

    print("\n❌ You ran out of attempts!")
    print("The secret code was:", " ".join(secret))


# -----------------------------------------
# Run game
# -----------------------------------------
if __name__ == "__main__":
    play_mastermind()
