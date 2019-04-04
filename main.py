import clientchat
from serialchat import *
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
    serial_chat = SerialChat(ConsoleConnection())

    is_answered = False

    def lol_handle(update, chat):
        chat.send('Work')

    serial_chat.dispatcher.add_handler(CommandTypeHandler('aha', lambda u, c: c.send('ohoho')))
    serial_chat.dispatcher.add_handler(CommandTypeHandler('Lol', lol_handle))
    serial_chat.dispatcher.add_handler(CommandTypeHandler('Kek', lambda u, c: c.send('Kirill petux')))
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


if __name__ == '__main__':
    main()
