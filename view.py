def view_menu():
    print("HANGMAN")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Quit")
    
def view_quit():
    print("Goodbye!")
    quit()

def view_game_choice(dificulty):
    print("You chose ", dificulty, " difficulty")

def view_category():
    print ("Choose a category:")
    print ("1. Countries")
    print ("2. Capitals")
    print("3. Go back")

def view_difficulty_choice(difficulty):
    print("You chose ", difficulty, " difficulty")
   
def view_category_choice(category):
    print("You chose ", category)
    print("Good luck!")

def view_word_to_guess(word_list):
    length = len(word_list)
    for i in word_list:
        print(i, end=" ")

def good_message():
    print("Good Job")

def wrong_message():
    print("Wrong")

    
