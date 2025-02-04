from view import *
from model import *
from controller import *

def game():
    difficulty = 0
    lives = 0
    category = 0
    while difficulty == 0:
        difficulty = choose_difficulty()
        lives = set_lives(difficulty)
        if lives == 0:
            view_quit()
        else:
            view_category()
            category = choose_category()
            if category == "3":
                difficulty = 0
            elif category != "1" and category != "2":
                print("Invalid choice")
                category = 0
            else:
                view_difficulty_choice(difficulty)
                view_category_choice(category)
                word = get_word(c.FILE, category)
                print(word)
                print(change_word_to_list(word))
                view_word(change_word_to_list(word))
                while lives > 0:
                    letter = get_letter()
                    if check_letter(change_word_to_list(word), letter):
                        print("Good job!")
                    else:
                        lives -= 1
                        print("Wrong letter! You have ", lives, " lives left!")
                    if lives == 0:
                        print("You lost!")
                        break
                    if change_word_to_list(word) == []:
                        print("You won!")
                        break


def main():
    print("Welcome to Hangman!")
    game()
  

main()