# ftp_server
Python3 ftp server

## How to
Copy the myftpsrv.service file to '/etc/systemd/system/'
Run systemctl daemon-reload for the system to see the service unit
Run systemctl start myftpsrv
Run systemctl enable myftpsrv to autostart on boot
