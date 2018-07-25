"""Generate random name.

Names lib are from "https://github.com/joke2k/faker", only support name = firstname + lastname now.
"""
import random


from user.en_us_names_lib import (
    en_US_female_first_names, en_US_male_first_names, en_US_last_names
)


def generate_en_us_name(sex='F'):
    """
    :param sex: 'F'=female or 'M'=male
    :return:
    """
    first_name = random.choice(en_US_female_first_names) if sex == 'F' else random.choice(en_US_male_first_names)
    last_name = random.choice(en_US_last_names)
    return {
        'full_name': ' '.join([first_name, last_name]),
        'first_name': first_name,
        'last_name': last_name,
    }


if __name__ == '__main__':
    name = generate_en_us_name()
    print(name)
