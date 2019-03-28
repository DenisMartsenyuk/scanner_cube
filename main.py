import clientchat
from serialchat import SerialChat
import scanning
import threading

from time import sleep # todo: УБРАТЬ ПОТОМ

from queue import Queue

from config import *
from handlers import *


class Application(object):
    def __init__(self):
        pass


def main():
    serial_chat = SerialChat(Config.SerialChat.PORT, Config.SerialChat.BAUDRATE)
    serial_chat.connect()

    is_answered = False

    def pong_handle(update, chat):
        nonlocal is_answered
        is_answered = True
        print('Ponghandle ' + update)

    serial_chat.dispatcher.add_handler(CommandTypeHandler('Pong', pong_handle))
    serial_chat.stop_signal = Config.SerialChat.STOP_SIGNAL
    serial_chat.start()



    # serial_chat.dispatcher.add_handler(DefaultHandler())

    def feedback_send(data):
        nonlocal is_answered
        is_answered = False
        serial_chat.send(data)
        while not is_answered:
            pass
        print('Ohyett')

    while True:
        feedback_send('Ping')
    # client = clientchat.ClientChat(Config.ClientChat.HOST, Config.ClientChat.PORT)
    #serial_buffer = Queue()
    # client_buffer = Queue()

    # client.set_buffer(client_buffer)

    #serial.start()
    # client.start()

    # scan = scanning.Scan()
    # scan.set_send_serial(serial.feedback_write())
    # scan.set_send_client(client.send_data())
    # scan.start()
    ''' while True:
        sleep(1)
        while not serial.is_open:
            pass
        if serial.is_open:
            serial.feedback_write("LN")'''

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
