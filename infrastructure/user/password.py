import random


def generate_password():
    lowers = [chr(i) for i in range(97, 123)]
    uppers = [chr(i) for i in range(65, 91)]
    numbers = [chr(i) for i in range(48, 58)]
    symbols = [i for i in '!#$%^*()']

    parts = [lowers, uppers, symbols, numbers]
    pw = [''.join(random.choices(part, k=2)) for part in parts]
    password = ''.join(pw)
    password = ''.join(random.sample(password, k=len(password)))

    return {
        'password': password,
    }
