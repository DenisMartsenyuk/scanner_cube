import threading
import socket

from queue import Queue


class ClientChat(threading.Thread):

    def __init__(self, host, port):
        super(ClientChat, self).__init__()
        self.socket = socket.socket()
        self.daemon = True
        self.host = host
        self.port = port
        self.received_data = Queue()
        self.is_open = False

    def run(self):
        while True:
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            client, address = self.socket.accept()
            self.is_open = True
            while self.is_open:
                data = client.recv(1024)
                if data:
                    self.received_data.put(data.decode('utf-8'))
                else:
                    self.is_open = False
            self.socket.close()

    def send_data(self, data): # todo: проверить конвертацию данных
        if self.is_open:
            self.socket.send(data)
        else:
            raise Exception('Sending error')

    def set_buffer(self, buffer):
        self.received_data = buffer
