import os

path = input("Please input the directory path: ")
try:
    files = os.listdir(path)
    for file in files:
        print(file)
except FileNotFoundError:
    print("Directory not found")
