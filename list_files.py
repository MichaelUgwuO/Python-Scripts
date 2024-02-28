import os

def list_files(directory):
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            print(file)

list_files('.')
