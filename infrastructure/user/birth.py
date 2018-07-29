import random


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
