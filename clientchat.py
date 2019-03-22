import threading
import socket

from queue import Queue


class ClientChat(threading.Thread, socket.socket):

    def __init__(self, host, port):
        threading.Thread.__init__(self)
        socket.socket.__init__(self)
        self.daemon = True
        self.host = host
        self.port = port
        self.received_data = Queue()
        self.is_open = False

    def run(self):
        while True:
            self.bind((self.host, self.port))
            self.listen(1)
            client, address = self.accept()
            self.is_open = True
            while self.is_open:
                data = client.recv(1024)
                if data:
                    self.received_data.put(data.decode('utf-8'))
                else:
                    self.is_open = False
            self.close()

    def send_data(self, data): ##проверить конвертацию данных
        if self.is_open:
            self.send(data)

    def set_buffer(self, buffer):
        self.received_data = buffer
