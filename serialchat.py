import threading
import serial
from time import sleep

from queue import Queue
from handlers import *
# [Type]: [data] [stop sig]
from config import *


class Connection(object):
    def connect(self):
        pass

    def send(self, data):
        pass

    def read(self):
        pass


class ConsoleConnection(Connection):
    def send(self, data):
        print('->', data)

    def read(self):
        return input()


class SerialChat(threading.Thread):

    '''
        Handle communication with serial port.

        Args:
            connection(Connection): connection
        Attributes:
        todo: pointless docs :( Who need docs?
    '''

    def __init__(self, connection: Connection):
        super(SerialChat, self).__init__()
        self.connection = connection
        self.dispatcher = SerialDispatcher(self)

    def send(self, data):
        self.connection.send(data)

    def run(self):
        while True:
            try:
                self.dispatcher.handle_update(self.connection.read())
            except Exception as exc:
                print('Reconnection')
                self.connection.connect()


class SerialDispatcher(object):
    def __init__(self, chat: SerialChat):
        self.chat = chat
        self.handlers = []

    def add_handler(self, handler):
        if not isinstance(handler, Handler):
            raise TypeError
        self.handlers.append(handler)

    def handle_update(self, update: str):
        for handler in self.handlers:
            if handler.check_update(update, self.chat):
                handler.handle_update(update, self.chat)
