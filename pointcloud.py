from config import *


class Point3D(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class PointCloud(list):

    def save_file(self):
        # todo: сохранить в файл
        pass
