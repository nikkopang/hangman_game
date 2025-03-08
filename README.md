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
A simple Hangman game written in Python. You can play the game either on your terminal or on your [browser via Shiny](https://npcodes.shinyapps.io/shiny_hangman/)!

## Pre-requisites
In order to run the code locally, you need to install the following packages:
- pandas
```python
pip install pandas
```
- shiny
```python
pip install shiny
```

## Installation
1. Clone the repository: `git clone https://github.com/nikkopang/hangman_game.git`
2. Install the open source shiny package: `pip install shiny`
3. Run the game: `shiny run app.py`


## Usage
- Start the game by running `shiny run app.py` in your terminal or using your [browser](https://npcodes.shinyapps.io/shiny_hangman/).
- Choose your game mode: Short or Long (this determines your max number of guesses for the game)
- Click on the `Start Game` button to start a new game.
- Guess the word, and any matching letters will fill in the word.
- You can also allow additional hints, which will show you all the mismatched letters that you used in your previous guesses.
