#!/usr/bin/env python3

import threading


class UART_thread(threading.Thread):
    def run(self):
        print('UART threadaaa')


class TCP_IP_thread(threading.Thread):
    def run(self):
        print('TCP/IP thread')
