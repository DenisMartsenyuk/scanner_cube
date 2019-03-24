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
        self.last_bytes = None
        self.stop_signal = ''
        self.daemon = True

    def set_connection(self):
        self.close()
        while not self.is_open:
            try:
                self.open()
                print('Connected to serial')
            except Exception:
                pass
                # print("fuck this")
                # sleep(0.1)

    def set_buffer(self, buffer):
        self.received_data = buffer

    def set_stop_signal(self, stop_signal):
        self.stop_signal = stop_signal


    def feedback_write(self, data):
        data = data + self.stop_signal
        bytes_data = data.encode('utf-8')
        self.last_bytes = data
        self.write(bytes_data)
        print("send")
        while self.last_bytes is not None:
            pass
            # print("lol")
            # sleep(0.1)
        print('I poluchil')
        # sleep()

    def lol(self, data):
        print(data)

        self.write(data)

    def run(self):
        while True:
            print("potoook")
            try:
                data = self.read_until(self.stop_signal.encode('utf-8'))
                print(data.decode('utf-8'))

                if self.last_bytes:
                    print("IN this")

                if self.last_bytes == data:
                    print("DADADADADA")
                    self.last_bytes = None
                else:
                    # print(data)
                    # print("Prishlo")
                    self.received_data.put(data.decode('utf-8'))
            except Exception:
                print("Fuck")
                self.set_connection()
