#author : Nexarque
#date : 2 september 2025


import socket 
target = "127.0.0.1"  
ports = [21, 22, 25, 80, 443, 8080]

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    try: 
        scanner.connect((ip, port))
        print(f"[+] Port {port} is Open ")
    except:
        print(f"[-] Port {port} is Closed ")
    finally:
        scanner.close()

target = input("Enter the IP to scan : ")
print(f"Scanning target : {target}")
for port in ports :
    scan_port(target, port)