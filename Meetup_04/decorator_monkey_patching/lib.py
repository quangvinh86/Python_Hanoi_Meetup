import random


class LimitError(Exception):
    pass


def query_user_data(name):
    choice = random.randrange(1, 7)
    if choice == 1:
        raise LimitError
    else:
        return 'User data of {}: {}'.format(name, choice)


def query_team_data():
    choice = random.randrange(1, 7)
    if choice == 1:
        raise LimitError
    else:
        return 'User data'
