class Config:

    class SerialChat:
        PORT = '/dev/tty.usbserial-1460'
        BAUDRATE = 9600
        STOP_SIGNAL = '/'

    class ClientChat:
        HOST = 'localhost'
        PORT = 9090