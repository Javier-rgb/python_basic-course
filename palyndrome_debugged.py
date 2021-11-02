def is_palyndrome(str):
    try:
        if len(str) == 0:
            raise ValueError("An empty void cannot be entered")
        return str == str[::-1]
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        print(is_palyndrome(""))
    except TypeError:
        print("only string are allowed")


if __name__ == '__main__':
    run()