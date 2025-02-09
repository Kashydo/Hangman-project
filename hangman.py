from view import *
from model import *
from controller import *
import constants as c



def main():
    print("Welcome to Hangman!")
    while True:
        difficulty = choose_difficulty()
        if difficulty == "4":
            view_quit()
            break
        view_category()
        category = choose_category()
        if category == "3":
            continue
        lives = set_lives(difficulty)
        word = get_word(c.FILE, category)
        game(word, lives)
        play_again = input("Do you want to play again? (y/n)")
        if play_again.lower() == "n":
            view_quit()
            break
        else:
            continue
  

main()