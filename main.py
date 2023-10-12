def say_hello(name: str):
    print(f'Привет {name}')


def main():
    name = input('Пожалуйста введите ваше имя: ')
    say_hello()
    input('Press Enter для входа ..')


if __name__ == '__main__':
    main()