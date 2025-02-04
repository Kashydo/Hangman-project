import constants as c
import pandas as pd
import random
from controller import *
from view import *

def set_lives(difficulty):
    lives = 0
    while lives == 0:
        if difficulty == "1":
            lives = c.EASY["lives"]
        elif difficulty == "2":
            lives = c.MEDIUM["lives"]
        elif difficulty == "3":
            lives = c.HARD["lives"]
        elif difficulty == "4":
            break
    return lives
   

def count_records(file):
    data = pd.read_csv(file)
    return len(data)

def get_word(file, category):
    data = pd.read_csv(file)
    index = random.randint(0, count_records(file))
    column_names = list(data.columns)
    if category == "1":
        word = data[column_names[0]][index]
    if category == "2":
        word = data[column_names[1]][index]
    return word.replace(" ", "")
    
def change_word_to_list(word):
    return list(word.lower())

def check_letter(word_list, letter):
    if letter in word_list:
        return True
    else:
        return False

