def divisors(num):
    divisors = []

    assert num > 0, "A Natural number must be entered"
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input("Type a number: ")
    assert num.lstrip('-').isnumeric(), "A number must be entered"
    num = int(num)
    print(divisors(num))
    print("Program ends")
        

if __name__ == '__main__':
    run()