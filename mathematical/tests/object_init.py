from mathematical.trigonometry import Point

NewTestPoint(object):
    point_a = None
    point_b = None

    def init_new_points(self):
        self.point_a = Point(5,7)
        self.point_b = Point(4,10)

    def get_sum(self):
        x = 5+4
        y = 7+10
        return x, y

    def get_sub(self):
        x = 5-4
        y = 7-10
        return x, y
