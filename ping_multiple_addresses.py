import subprocess

# List of hosts to ping
hosts = ['8.8.8.8', '1.1.1.1', '192.168.1.1']

for host in hosts:
    result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE)
    if result.returncode == 0:
        print(f'{host} is up')
    else:
        print(f'{host} is down')
