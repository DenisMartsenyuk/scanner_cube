import threading


class Scan(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.is_scanning = False
        self.send_function = None
        self.angle = None
        self.turn_angle = None

    def set_send_function(self, function):
        self.send_function = function

    def set_angle(self, angle):
        self.angle = angle

    def set_turn_angle(self, turn_angle):
        self.turn_angle = turn_angle

    def start_scan(self):
        self.is_scanning = True

    def stop_scan(self):
        self.is_scanning = False
        self.angle = None
        self.turn_angle = None

    def run(self):
        while self.is_scanning:
            pass