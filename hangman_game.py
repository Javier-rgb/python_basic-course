import random

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

def get_position(x, array):
    for i, value in enumerate(array):
        if value == x:
            print(i)



def write():
    pass

def run():
    num = random.randint(0, 170)
    print("Welcome to Hangman Game")

    #secret_word = get_word(num)

    secret_word = "Manzana "
    new_array = list(secret_word)

    new_array.pop(len(new_array) - 1)

    empty = display_screen(new_array)

    #new_dix = {letter: new_array.index(letter) for letter in new_array}

    get_position('a', new_array)

    print(secret_word)
    print(new_array)
    print(len(new_array))
    # print(new_dix)
    print(empty)



if __name__ == '__main__':
    run()