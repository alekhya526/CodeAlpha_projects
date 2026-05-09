import random

# Word list by difficulty
words = {
    "easy": ["cat", "dog", "sun", "pen"],
    "medium": ["apple", "tiger", "chair", "plane"],
    "hard": ["python", "program", "developer", "algorithm"]
}

# Hangman stages
stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

def play_game():
    print("🎮 Welcome to Advanced Hangman!")

    # Choose difficulty
    level = input("Choose difficulty (easy / medium / hard): ").lower()
    if level not in words:
        level = "medium"

    word = random.choice(words[level])
    guessed = []
    attempts = 6

    while attempts > 0:
        print(stages[6 - attempts])
        
        display = ""
        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "
        
        print("\nWord:", display.strip())
        print("Used letters:", guessed)

        if "_" not in display:
            print("🎉 You WON! The word was:", word)
            return

        guess = input("Enter a letter: ").lower()

        if guess in guessed:
            print("⚠ Already guessed!")
            continue

        guessed.append(guess)

        if guess not in word:
            attempts -= 1
            print("❌ Wrong guess! Attempts left:", attempts)

    print(stages[-1])
    print("💀 You LOST! The word was:", word)


def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing!")
            break

main()