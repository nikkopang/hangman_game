# Hangman Game
<pre>
 __   __  _______  __    _  _______  __   __  _______  __    _         +---------------+
|  | |  ||   _   ||  |  | ||       ||  |_|  ||   _   ||  |  | |        |               :
|  |_|  ||  |_|  ||   |_| ||    ___||       ||  |_|  ||   |_| |        |              ---
|       ||       ||       ||   | __ |       ||       ||       |        |             |   |
|       ||       ||  _    ||   ||  ||       ||       ||  _    |        |              ---
|   _   ||   _   || | |   ||   |_| || ||_|| ||   _   || | |   |        |               |
|__| |__||__| |__||_|  |__||_______||_|   |_||__| |__||_|  |__|        |             / | \
 _______  _______  __   __  _______                                    |            /  |  \
|       ||   _   ||  |_|  ||       |                                   |               |
|    ___||  |_|  ||       ||    ___|                                   |              / \
|   | __ |       ||       ||   |___                                    |             /   \
|   ||  ||       ||       ||    ___|                                   |
|   |_| ||   _   || ||_|| ||   |___                                    |
|_______||__| |__||_|   |_||_______|                                 =========================
</pre>

## Badges
![Static Badge](https://img.shields.io/badge/Language-Python-blue)
![Static Badge](https://img.shields.io/badge/Created_Date-March_2025-brightgreen)

## Description
A simple command-line Hangman game written in Python. You can play the game either on your terminal or on your browser via Shiny!

## Installation
1. Clone the repository: `git clone https://github.com/nikkopang/hangman_game.git`
2. Install the open source shiny package: `pip install shiny`
3. Run the game: `shiny run app.py`

## Usage
- Start the web app by running `shiny run app.py`.
- Choose your game mode: Long or Short (this determines your max number of guesses)
- Click on the `Start Game` button.
- Guess the word, and any matching letters will fill in the word.
- You can also allow additional hints, which will show you all the mismatched letters that you used in your previous guesses.
