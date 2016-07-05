import socket
import threading
import time
import logging

HOST = ''
PORT = 8018
TIMEOUT = 5
BUF_SIZE = 1024

class WhatsUpServer(threading.Thread):

    def__init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.ip = self.addr[0]
        self.name = ''

    def print_indicator(self, prompt):
        self.conn.send('%s\n>> ' %(prompt,))

    def login(self):
        global clients
        global messages
        global acounts
        global onlines

        logging.info('Connected from: %s:%s' %(self.addr[0], self.addr[1]))
        clients.add((self.conn, self.addr))
        msg = '\n## Welcome to WhatsUp\n## Enter `!q` to quit\n'

        # new user
        print accounts
        if self.ip not in accounts:
            msg += '##Please enter your name: '
            self.print_indicator(msg)
            account[self.ip] = {
                'name': '',
                'pass': '',
                'lastlogin': time.ctime()
                
                }
                while 1:
                    name = self.conn.recv(BUF_SIZE).strip()
                    if name in messages:
                        self.print_indicator('## This name already exists, please try another')

                    else:
                        break
                    accounts[self.ip]['name'] = name
                    self.name = name
                    logging.info('%s logged as %s' % (self.addr[0], self.name,))
                    messages[name] = []
                    self.print_indicator('## Hello %s, please enter your password: %(self.name)')
        
