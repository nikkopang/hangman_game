from shiny_hangman.hangman_states import get_hangman_states
from shiny_hangman.utils import get_random_word, check_letters_found_in_word

def set_game_mode():
    user_in = ""
    while user_in not in ["long", "short"]:
        print("What game mode would you like? Choose either long or short.")
        user_in = input("Game mode: ").strip().lower()

    print(f"Game mode set to '{user_in}'.")
    return user_in

def get_user_in(word_length):
    user_in = input("Guess a word: ").lower().strip()

    while len(user_in) != word_length:
        print(f"Please enter a {word_length} letter word.")
        user_in = input("Guess a word: ").lower().strip()

    return user_in

def run_terminal_game():
    selected_word = get_random_word().lower() # Get random 5 letter word
    
    # Initialise game criterias
    is_correct = False
    current_word = ["_"] * len(selected_word)
    game_mode = set_game_mode()

    # Display the current board state
    hangman = get_hangman_states(game_mode)
    attempts = 0

    game_running = True
    while game_running:
        board = hangman[attempts]
        print(board) # Show hangman state
        
        # Allow user to guess
        print(f"Current word: {current_word}")
        user_in = get_user_in(len(selected_word))

        # Check answer
        if user_in == selected_word:
            is_correct = True
            game_running = False

        # Show hints based on any matching letters 
        matched_letters = check_letters_found_in_word(user_in, selected_word)

        if len(matched_letters) > 0:
            for idx, letter in enumerate(list(selected_word)):
                if current_word[idx] != "_":
                    continue
                elif letter in matched_letters:
                    current_word[idx] = letter
        
        attempts += 1
        if attempts == len(hangman): # End the game if too many attempts made
            game_running = False
    
    # Game end message
    if is_correct:
        print(f"CONGRATULATIONS! You guessed the correct word: {selected_word}")
    else:
        print(f"OH NO! The word was {selected_word}. Try again next time.")

run_terminal_game()