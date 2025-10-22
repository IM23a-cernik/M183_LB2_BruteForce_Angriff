import os, string

instances = int(input("Number of instances:"))
chars = string.ascii_letters + string.digits + string.punctuation

for i in range(instances):
    start_char = chars[i]
    os.system(f'start cmd /k "python script.py {start_char}"')