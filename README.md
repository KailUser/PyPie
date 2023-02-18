
# PyPie

PyPie is a Python-based command-line tool that allows you to check the status of a website, scan ports, and connect to an FTP server.
## Installation

To use PyPie, you will need to have Python 3.x installed on your system. Once you have Python installed, simply download the pypie.py file from the repository and save it to your local machine.
## Usage

To use PyPie, navigate to the directory where you saved pypie.py and run the following command:

```bash
  python index.py
```
This will launch PyPie and display a menu of options:
```bash
Welcome to PyPie   
1. Check site status
2. Check port
3. Connect to ftp
4. Exit
```
Select one of the options to perform the corresponding action.
## Check site status

Selecting option 1 will allow you to check the status of a website. You will be prompted to enter the URL of the website you want to check. PyPie will then attempt to connect to the website and retrieve the response code. If the response code is 200, the website is considered to be available. Otherwise, PyPie will report that the website is not available along with the response code.
## Check port

Selecting option 2 will allow you to scan a port on a website. You will be prompted to enter the URL of the website and the port you want to scan. PyPie will then attempt to connect to the specified port on the website. If the connection is successful, PyPie will report that the port is open. Otherwise, PyPie will report that the port is not open.
## Connect to FTP

Selecting option 3 will allow you to connect to an FTP server. You will be prompted to enter the server address, username, and password. Once you have successfully connected to the server, you will be able to download and upload files to and from the server.
## License

PyPie is released under the MIT License. See [LICENSE](https://raw.githubusercontent.com/KailUser/PyPie/alpha/LICENSE) for details.
