import threading
import serial
from time import sleep

from queue import Queue
from handlers import *
# [Type]: [data] [stop sig]


class SerialChat(threading.Thread):

    '''
        Handle communication with serial port.

        Args:
            port_path(str): port
            baudrate(int): port baudrate

        Attributes:
            serial(serial.Serial): port
            received_data(Queue): data from port
        todo: pointless docs :( Who need docs?
    '''

    def __init__(self, port_path, baudrate):
        super(SerialChat, self).__init__()

        self.serial = serial.Serial()
        self.serial.baudrate = baudrate
        self.serial.port = port_path

        self.received_data = Queue()
        self.last_bytes = None
        self.stop_signal = ''
        self.dispatcher = SerialDispatcher(self)

    def connect(self):
        self.serial.close()
        while not self.serial.is_open:
            try:
                self.serial.open()
            except serial.SerialException as exc:
                print(exc)
                # print("fuck this")
                # sleep(0.1)
            else:
                print('Connected to serial')

    def set_buffer(self, buffer): # property!
        self.received_data = buffer

    '''def set_stop_signal(self, stop_signal): # property!
        self.stop_signal = stop_signal'''

    def feedback_write(self, data):
        data = data + self.stop_signal
        bytes_data = data.encode('utf-8')
        self.last_bytes = data
        self.serial.write(bytes_data)
        print("send")
        while self.last_bytes is not None:
            pass
            # print("lol")
            # sleep(0.1)
        print('I poluchil')
        # sleep()

    def send(self, data: str):
        print('->', data)
        if data.startswith('Ping'):
            sleep(1)
            self.dispatcher.handle_update('Pong ' + data)
       # self.serial.write(bytes(data, 'utf-8'))

    def run(self):
        while True:
            pass
           # print("poto2ook")
            #data = input()
            #print('Data:' + data)
            #self.dispatcher.handle_update(data)

    @property
    def is_open(self):
        return self.serial.is_open


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
