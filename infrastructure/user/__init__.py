from user.birth import generate_birth
from user.name import generate_en_us_name
from user.password import generate_password


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


if __name__ == '__main__':
    user = generate_user()
    print(user)
