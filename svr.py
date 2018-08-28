#!/usr/bin/python3

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def myftpserv():
    authorizer = DummyAuthorizer()
    authorizer.add_user('user1', 'XXXXXX', '/home/user1', perm='elradfmwMT')
    authorizer.add_user('user2', 'XXXXXX', '/home/user2', perm='elradfmwMT')
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = 'FTP server, unauthorised access prohibited!'
    handler.passive_ports = range(60000, 61000)
    address = ('', 2121)
    server = FTPServer(address, handler)
    server.max_cons = 256
    server.max_cons_per_ip = 5
    server.serve_forever()


if __name__ == '__main__':
    myftpserv()
