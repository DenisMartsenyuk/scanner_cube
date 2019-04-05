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

    # adding handlers

    def feedback(func):
        def f(*args, **kwargs):
            nonlocal is_answered
            is_answered = True
            return func(*args, **kwargs)

        return f

    @feedback
    def rotate_handle(update, chat):
        pass

    @feedback
    def lazer_handle(update, chat):
        pass

    @feedback
    def gohome_handle(update, chat):
        pass

    @feedback
    def move_handle(update, chat):
        pass

    @feedback
    def lid_handle(update, chat):
        pass

    serial_chat.dispatcher.add_handler(CommandTypeHandler('Rotate', rotate_handle))
    serial_chat.dispatcher.add_handler(CommandTypeHandler('Lazer', lazer_handle))
    serial_chat.dispatcher.add_handler(CommandTypeHandler('Go home', gohome_handle))
    serial_chat.dispatcher.add_handler(CommandTypeHandler('Lid', lid_handle))

    serial_chat.start()

    is_answered = False

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
