import os

if __name__ == '__main__':
    print("Welcome to Robot Speaker 1.1. Created by Ayushman")
    while True:
        x = input("Enter your speech: ")
        command = f'say "{x}"'
        os.system(command)