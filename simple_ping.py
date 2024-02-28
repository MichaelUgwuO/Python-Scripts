import subprocess

def ping(host):
    response = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE)
    if response.returncode == 0:
        print(f"{host} is reachable")
    else:
        print(f"{host} is not reachable")

user_input_website = input("Enter the website URL: ")
ping(user_input_website)
