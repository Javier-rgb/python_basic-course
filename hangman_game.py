import random
import os

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

def check_letter(x, array, empty):
    for i, value in enumerate(array):
        if value == x:
            empty[i] = x


def run():
    num = random.randint(0, 170)   

    secret_word = get_word(num)

    secret_array = list(secret_word)
    secret_array.pop(len(secret_array) - 1) # Removing '\n'

    empty = display_screen(secret_array)

    while empty != secret_array:
        print("Welcome to Hangman Game")
        print(secret_array)
        print(empty)

        letter = input("type a letter: ")
        check_letter(letter, secret_array, empty)
        os.system("clear")


if __name__ == '__main__':
    run()