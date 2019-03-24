import clientchat
import serialchat
import scanning
import threading

from time import sleep #УБРАТЬ ПОТОМ

from queue import Queue

from config import *


def kek(serial):
    while True:
        # sleep(1)
        # if serial.is_open:
        #     serial.feedback_write("LN")
        #     while serial.last_bytes:
        #         pass
            print('kek')

def main():

    serial = serialchat.SerialChat(Config.SerialChat.PORT, Config.SerialChat.BAUDRATE)
    #client = clientchat.ClientChat(Config.ClientChat.HOST, Config.ClientChat.PORT)

    serial_buffer = Queue()
    #client_buffer = Queue()

    serial.set_stop_signal(Config.SerialChat.STOP_SIGNAL)
    serial.set_buffer(serial_buffer)
    #client.set_buffer(client_buffer)

    serial.start()
    #client.start()

    # scan = scanning.Scan()
    # scan.set_send_serial(serial.feedback_write())
    # scan.set_send_client(client.send_data())
    # scan.start()


    while True:
        sleep(1)
        while not serial.is_open:
            pass
        if serial.is_open:
            serial.feedback_write("LN")

        # sleep()
        # if not serial_buffer.empty():
        #     print(serial_buffer.get())
        # else:
        #     print('XER')
        # if serial.is_open:
        #      # pass
        #     serial.feedback_write("LN")
            #
            # print("iopen")
        # sleep(1)
        # if serial.is_open:
        #     serial.feedback_write("LN")
        #     while serial.last_bytes:
        #         pass
        #     print('kek')
        # serial.lol("LN/".encode('utf-8'))
        ##print("loloooo")



if __name__ == '__main__':
    main()
