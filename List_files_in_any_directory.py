import os

def list_files(directory):
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            print(file)

user_input_directory = input("Enter the directory path: ")
list_files(user_input_directory)
