import socket

host = 'scanme.nmap.org'
ports = [22, 80, 443]

for port in ports:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f'Port {port} is open')
        else:
            print(f'Port {port} is closed')
