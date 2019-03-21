import clientchat
import serialchat
import scanning

from queue import Queue

from config import *


def main():

    serial = serialchat.SerialChat(Config.SerialChat.PORT, Config.SerialChat.BAUDRATE)
    client = clientchat.ClientChat(Config.ClientChat.HOST, Config.ClientChat.PORT)

    serial_buffer = Queue()
    client_buffer = Queue()

    serial.set_buffer(serial_buffer)
    client.set_buffer(client_buffer)

    serial.start()
    client.start()

    scan = scanning.Scan()
    scan.set_send_serial(serial.feedback_write())
    scan.set_send_client(client.send_data())
    scan.start()

    while True:
        pass


if __name__ == '__main__':
    main()
