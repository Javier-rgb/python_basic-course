from functools import reduce

def run():
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    odd = [i for i in my_list if i % 2 != 0]

    odd_ho = list(filter(lambda x: x % 2 != 0, my_list))

    my_list_five = [i**2 for i in my_list]

    ho_my_list = list(map(lambda x: x**2, my_list))

    total = reduce(lambda a, b: a + b, my_list)

    print(odd)
    print(odd_ho)
    print(my_list_five)
    print(ho_my_list)
    print(total)


if __name__ == '__main__':
    run()