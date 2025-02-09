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
    return word

def is_letter_used(letter, used_list):
    return used_list.count(letter) > 0

def prepare_word(word):
    word_list =[]
    for i in word:
        if i.isalpha():
            word_list.append('_')
        else:
            word_list.append(i)
    return word_list

def check_if_letter_in_word(word, letter): 
    return word.lower().count(letter) > 0

def game(word, lives):
    used_letters=[]
    word_list = prepare_word(word)
    letters_left = len(word.replace(" ",""))
    while lives > 0 and letters_left > 0:
        letter = ""
        print(word)
        view_word_to_guess(word_list)
        while letter=="":
            letter = get_letter()
            if letter in used_letters:
                print("You already used this letter")
                letter = ""
        used_letters.append(letter)
        if check_if_letter_in_word(word,letter):
            print("Good Job")
            for  i in range(len(word)):
                if word[i].lower() == letter:
                    word_list[i] = letter
                    letters_left -= 1
        else:
            print("Wrong")
            lives -= 1
    if letters_left == 0:
        print("You won!")
    else:
        print("You lost!")