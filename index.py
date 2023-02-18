import requests
import os
import socket
from ftplib import FTP

while True:
    os.system('cls')
    print("""Welcome to PyPie   
    1. Check site status
    2. Check port
    3. Connect to ftp
    4. Exit""")
    option = input('> ')
    if option == "1":
        website = input('WebSite url: ')
        try:
            response = requests.get(website)
            if response.status_code == 200:
                print(f"The website {website} is available")
            else:
                print(f"The website {website} is not available ({response.status_code})")
        except requests.ConnectionError:
            print(f"The website {website} is not available")
    elif option == '2':
        website = input('WebSite url: ')
        port = input('Port for scanning: ')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((website, port))
            print(f"The port {port} on website {website} is open")
        except socket.error:
            print(f"The port {port} on website {website} is not open")
        s.close()
    elif option == '3':
        ftp_server = input('FTP server: ')
        username = input('Username: ')
        password = input('Password: ')
        # Connect to the FTP server
        ftp = FTP(ftp_server)
        ftp.login(user=username, passwd=password)

        # List the contents of the current directory on the FTP server
        ftp.retrlines("LIST")
        print(f'Welcome to ftp server {ftp_server}\n1. Download file\n2.Upload\n3.Exit')
        while True:
            option = input('> ')
            if option == '1':
                filename = input('File name: ')
                with open(filename, "wb") as f:
                    ftp.retrbinary(f"RETR {filename}", f.write)
            elif option == '2':
                filename = input('File to upload: ')
                with open(filename, "rb") as f:
                    ftp.storbinary(f"STOR {filename}", f)
            elif option == '3':
                ftp.close()
    elif option == '4':
        break
    else:
        print('Command not found.')