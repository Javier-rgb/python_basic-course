def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"fisrt_name": "Javier", "last_name": "Gamez"}

    super_list = [
        {"fisrt_name": "Javier", "last_name": "Gamez"},
        {"fisrt_name": "Vanessa", "last_name": "Gutierrez"},
        {"fisrt_name": "Mariana", "last_name": "Encinas"},
    ]

    super_dict = {
        "my_list": [1, "hello", True, 4.5], 
        "int_nums": [1, 2, 3, 4, 5],
        "float_nums": [1.2, 5.5, 7.4]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == '__main__':
    run()

