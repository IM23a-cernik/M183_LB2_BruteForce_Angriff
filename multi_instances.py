import os
import string
import subprocess
import sys
from multiprocessing import Process


def run_instance(start_char):
    with open(f"output_{start_char}.log", "w", encoding="utf-8") as log:
        subprocess.Popen([sys.executable, "script.py", start_char],
                         stdout=log, stderr=log)


if __name__ == "__main__":
    instances = int(input("Number of instances: "))

    turkish = "çğıöşüÇĞİÖŞÜ"
    cyrillic_upper = "".join(chr(cp) for cp in range(0x0410, 0x042F + 1))
    cyrillic_lower = "".join(chr(cp) for cp in range(0x0430, 0x044F + 1))
    cyrillic = cyrillic_upper + cyrillic_lower
    chars = string.ascii_letters + string.digits + string.punctuation + turkish + cyrillic

    for c in chars:
        log_file = f"output_{c}.log"
        if os.path.exists(log_file):
            os.remove(log_file)

    if instances == 1:
        skip = 1
    else:
        skip = (len(chars) - 1) // (instances - 1)
    for i in range(instances):
        index = round(i * skip)
        start_char = chars[index]
        Process(target=run_instance, args=(start_char,)).start()
