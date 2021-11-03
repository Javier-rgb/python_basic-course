import random

def get_word(num):
    with open("./files/DATA.txt", "r") as sw:
        for i, value in enumerate(sw):
            if i == num:
                return value

def run():
    num = random.randint(0, 170)
    print("Welcome to Hangman Game")

    secret_word = get_word(num)
    new_array = list(secret_word)

    new_array.pop(len(new_array) - 1)

    print(secret_word)
    print(new_array)
    print(len(new_array))


if __name__ == '__main__':
    run()