def divisors(num):
    try:
        if num < 1:
            raise ValueError("A Natural number must be entered")
        divisors = []

        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        num = int(input("Type a number: "))
        print(divisors(num))
        print("Program ends")
    except ValueError:
        print("A number must be entered")
        


if __name__ == '__main__':
    run()