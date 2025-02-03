def menu(difficulty):
    lives = 0
    while lives == 0:
        if difficulty == "1":
            lives = 10
        elif difficulty == "2":
            lives = 7
        elif difficulty == "3":
            lives = 5
        elif difficulty == "4":
            quit()
        else:
            print("Invalid choice")
    return lives
   
def game(lives, word):
    # print word to guess
    # print lives
    # ask for a letter
    # check if letter is in word
    # if letter is in word, print letter in word
    # if letter is not in word, print "Letter not in word"