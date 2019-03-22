import threading
import serial
from time import sleep

from queue import Queue


class SerialChat(threading.Thread, serial.Serial):

    def __init__(self, serial_port, baudrate):
        threading.Thread.__init__(self)
        serial.Serial.__init__(self)
        self.port = serial_port
        self.baudrate = baudrate
        self.received_data = Queue()
        self.last_command = None

    def set_connection(self):
        self.close()
        while not self.is_open:
            try:
                self.open()
            except Exception:
                sleep(0.1)

    def set_buffer(self, buffer):
        self.received_data = buffer

    def feedback_write(self, data):
        self.last_command = data
        self.write(data)
        # преобразовать данные
        while self.last_command:
            pass

    def run(self):
        while True:
            try:
                data = self.readline()
                if self.last_command == data:
                    self.last_command = None
                else:
                    self.received_data.put(data)
            except Exception:
                self.set_connection()
