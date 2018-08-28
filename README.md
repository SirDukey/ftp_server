# ftp_server
Python3 ftp server

## Dependancies
* python3
* pyftpdlib

## How to (linux OS)
1. vim svr.py (add users, set passwords, set directories)
2. cp myftpsrv.service /etc/systemd/system/
3. systemctl daemon-reload
4. systemctl start myftpsrv
5. systemctl enable myftpsrv
6. forward ports 2121 to your server ip (for passive connections forward ports 60000 - 61000 aswell)

## How to (Windows)
1. get Python3 for windows
2. get git for windows
3. run python3 srv.py from a terminal
