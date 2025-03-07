from shiny.express import input, render, ui
from shiny import reactive

from hangman_states import get_hangman_states
from utils import get_random_word, check_letters_found_in_word

# INITIALISE PARAMS --------------
attempts = reactive.value(0)
selected_word = reactive.value("")
current_word = reactive.value([])
wrong_letters = reactive.value([])

is_correct = reactive.value(False)
game_running = reactive.value(False)

# UI -----------
ui.page_opts(title="Hangman Game", fillable=True)

# Sidebar code
with ui.sidebar():
    ui.input_selectize("game_mode", "Game mode:", choices=["Long", "Short"])
    ui.input_switch("enable_hints", "Enable hints?")

    ui.input_action_button("start_game", "Start Game")

# Main game area
@render.code
def show_board():
    states = get_game_states()
    num_of_attempts = attempts.get()
    board = states[num_of_attempts]

    if not game_running.get() and is_correct.get(): 
            # Game ended cuz of correct guess
            return board + "CONGRATS ON GUESSING THE WORD CORRECTLY!  ＼(＾O＾)／"
    elif not game_running.get() and selected_word.get() != "": 
            # Game ended cuz ran out of tries
            return board + f"Try again next time! The word was {selected_word.get()}"    
    elif game_running.get() and selected_word.get() != "": 
            # Game still running
            return states[num_of_attempts]

@render.text
def show_word():
    curr_word = current_word.get()
    curr_word = [l.upper() for l in curr_word]
    return f"Current word: {' '.join(curr_word)}"

@render.text
def show_hint():
    if input.enable_hints():
        unmatched_letters = wrong_letters.get()
        unmatched_letters = sorted(unmatched_letters)
        unmatched_letters = [l.upper() for l in unmatched_letters]
        return f"Previously used incorrect letters: {' '.join(unmatched_letters)}"

ui.input_text("user_in", "Guess a word:", "")

@render.ui
def _():
    if game_running.get():
        return ui.input_action_button("submit", "Submit")



# CALCS --------------
@reactive.effect
@reactive.event(input.start_game)
def _():
    word = get_random_word()
    selected_word.set(word)

    curr_word = ["_"] * len(word)
    current_word.set(curr_word)
    
    attempts.set(0)
    wrong_letters.set([])
    is_correct.set(False)
    game_running.set(True)

@reactive.calc
def get_game_states():
    states = get_hangman_states(input.game_mode().lower())
    return states

@reactive.effect
@reactive.event(input.submit, )
def check_guess():
    if not game_running.get(): # Game has not started yet.
        return

    # Get the current chosen word for the game
    correct_word = selected_word.get() 
    
    # Get user input
    user_in = input.user_in().lower().strip()

    # Check whether the user answered correctly
    if user_in == correct_word:
        current_word.set(list(correct_word))
        is_correct.set(True)
        game_running.set(False)
        return # Game ends
    
    # Make sure the user inputs a word that's the same length as the expected word
    elif len(user_in) != len(correct_word):
        ui.notification_show(f"Please enter a word that is {len(correct_word)} letter long.")
        return 
    
    # Incorrect guess - Check for any matching words
    matched_letters = check_letters_found_in_word(user_in, correct_word)

    # Update any used unmatched words for additional hints
    unmatched_letters = list(wrong_letters.get())
    for letter in set(user_in):
        if letter not in matched_letters and letter not in unmatched_letters:
            unmatched_letters.append(letter)
    wrong_letters.set(unmatched_letters)

    # Update the current word to show the hint of any matching letters found.
    if matched_letters != []:
        curr_word = list(current_word.get())
        for idx, letter in enumerate(list(correct_word)):
            if curr_word[idx] != "_":
                continue

            elif letter in matched_letters:
                curr_word[idx] = letter
        current_word.set(curr_word)
    
    num_of_attempts = attempts.get()
    num_of_attempts += 1
    attempts.set(num_of_attempts)
    
    max_attempts = len(get_game_states())
    if num_of_attempts == max_attempts-1:
        game_running.set(False)