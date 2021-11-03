import random

def get_word(num):
    secret_word = ""
    with open("./files/DATA.txt", "r") as sw:
        for i, value in enumerate(sw):
            if i == num:
                secret_word = value
                print(i + 1, secret_word)
                print(len(secret_word))

def run():
    num = random.randint(0, 170)
    print("Welcome to Hangman Game")

    get_word(num)


if __name__ == '__main__':
    run()