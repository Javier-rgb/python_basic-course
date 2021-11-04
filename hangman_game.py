import random
import os
import sys

def get_word(num):
    with open("./files/DATA.txt", "r") as sw:
        for i, value in enumerate(sw):
            if i == num:
                return value


def display_screen(word):
    empty = []
    for i in word:
        empty.append("_")
    return empty


def run():
    energy = 5   

    secret_word = get_word(random.randint(0, 170))
    secret_word = secret_word.upper()
    secret_array = list(secret_word)
    secret_array.pop(len(secret_array) - 1) # Removing '\n'

    empty = display_screen(secret_array)

    os.system("clear")
    
    while empty != secret_array:
        if energy == 0:
            print("You lose")
            sys.exit()
        
        print("Welcome to Hangman Game [type EXIT to quit] \tEnergy: " + str(energy))
        # print(secret_array)
        print(empty)

        empty_aux = empty.copy()

        letter = input("type a letter: ").upper()
        if letter == "EXIT":
            sys.exit()
        
        # check_letter(letter, secret_array, empty)
        for i, value in enumerate(secret_array):
            if value == letter:
                empty[i] = letter

        if empty_aux == empty:
            energy = energy - 1
        
        os.system("clear")


if __name__ == '__main__':
    run()