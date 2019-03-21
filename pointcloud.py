
class Point3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class PointCloud:

    def __init__(self):
        self.point_cloud = list()

    def add_point(self, point):
        self.point_cloud.append(point)