import string
import subprocess
import sys
from multiprocessing import Process

def run_instance(start_char):
    subprocess.Popen([sys.executable, "script.py", start_char],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    instances = int(input("Number of instances: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    if instances == 1:
        skip = 1
    else:
        skip = 92 // (instances - 1)

    for i in range(instances):
        index = round(i * skip)
        start_char = chars[index]
        Process(target=run_instance, args=(start_char,)).start()
