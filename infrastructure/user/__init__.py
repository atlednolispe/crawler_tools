<<<<<<< HEAD
from user.birth import generate_birth
from user.name import generate_en_us_name
from user.password import generate_password
=======
import random


from user.name import generate_en_us_name
>>>>>>> 04b11b2c227a22afd512f3a3ebb012230e678f4c


def generate_user(sex='F'):
    """
    :param sex:  'F'=female or 'M'=male
    :return:
    """
    user = {
        'sex': sex,
    }
    name = generate_en_us_name(sex)
    birth = generate_birth()
    password = generate_password()

    for d in [name, birth, password]:
        user.update(d)
    return user


<<<<<<< HEAD
=======
def generate_birth(start_year=1980, end_year=1995):
    year = str(random.randint(start_year, end_year))
    month = str(random.randint(1, 12))
    day = str(random.randint(1, 28))

    birth = {
        'year': year,
        'month': month,
        'day': day,
    }

    return birth


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


>>>>>>> 04b11b2c227a22afd512f3a3ebb012230e678f4c
if __name__ == '__main__':
    user = generate_user()
    print(user)
