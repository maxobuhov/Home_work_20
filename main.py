def say_hello(name: str):
    print(f'Hello {name}')


def main():
    name = input('Enter your name: ')
    say_hello()
    input('Press Enter to continue ...')


if __name__ == '__main__':
    main()