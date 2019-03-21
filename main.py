import clientchat
import serialchat
import scan

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

    def lol(data):
        serial.feedback_write(data)

    scan = scan.Scan(lol)

    while True:


    """lol = clientchat.ClientChat('localhost', 9090)
    lol.start()
    buffer = Queue()
    lol.set_buffer(buffer)
    ##ser = serialchat.SerialChat('/dev/tty.usbserial-1460', 9600)
    ##ser.start()
    ##lol = serialchat.Lol()

    while True:
        if(not buffer):
            print("plak plaka")
        else:
            while buffer.empty():
                print(buffer.get())
                ##print(x)
                ##print(" ")
            print("/n")
            ##print("have")
        sleep(0.5)"""


if __name__ == '__main__':
    main()
