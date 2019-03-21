import threading

import pointcloud


class Scan(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.is_scanning = False
        self.send_serial = None
        self.send_client = None
        self.angle = None
        self.turn_angle = None
        self.point_cloud = pointcloud.PointCloud()
        self.current_angle = 0

    def set_send_serial(self, function):
        self.send_serial = function

    def set_send_client(self, function):
        self.send_client = function

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
        self.point_cloud.clear()

    def get_2d_points(self):
        ##алгоритмы комп зрения. Выводят лист точек
        return 0

    def calculate_3d_points(self, points):
        ##пересчет в 3d
        pass

    def run(self):
        while True:
            while self.is_scanning and self.current_angle <= self.angle:

                self.calculate_3d_points(self.get_2d_points())

                self.current_angle += self.turn_angle
