import time

import lib


def retry_decor(func):
    def wrapper(*args, **kwargs):
        count = 0
        while True:
            try:
                result = func(*args, **kwargs)
                return result
            except lib.LimitError:
                count = count + 1
                wait = 2 ** count
                print("Failed, retrying the {} time, sleep for {}".format(count, wait))
                time.sleep(wait)

    return wrapper


lib.query_user_data = retry_decor(lib.query_user_data)


def main():
    for username in ['hvn', 'htl', 'tuda', 'hoangp']:
        response = lib.query_user_data(username)
        print(response)


if __name__ == "__main__":
    main()
