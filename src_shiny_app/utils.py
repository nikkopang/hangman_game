import random
import pandas as pd

def get_random_word(word_length=5):
    df = pd.read_csv("10000_Words.csv")
    df = df[df['words'].str.len() == word_length]
    word = random.choice(df.words.to_list())
    return word

def check_letters_found_in_word(word1, word2):
    letters = set(word1) # Get only the unique letters found in word1
    matched_letters = [letter for letter in letters if letter in word2]
    return matched_letters