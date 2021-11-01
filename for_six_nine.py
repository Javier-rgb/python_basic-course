def run():
    forsixnine = [i for i in range(1, 10001) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(forsixnine)

if __name__ == '__main__':
    run()