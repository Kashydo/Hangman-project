from view import *
from model import *
import constants as c
def choose_difficulty():
    difficulty = 0
    view_menu()
    while difficulty == 0:
        difficulty = input("Choose a difficulty level or quit:")
        if difficulty != "1" and difficulty != "2" and difficulty != "3" and difficulty != "4":
            print("Invalid choice")
            difficulty = 0
    return difficulty

def choose_category():
    category = input("Choose a category:")
    return category

def get_letter():
    letter = input("Enter a letter:")
    while letter.isalpha() == False or len(letter) != 1:
        print("Invalid input")
        letter = input("Enter a letter:")
    return letter.lower()


        
            
       