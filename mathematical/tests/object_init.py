from mathematical.trigonometry import Point

class NewTestPoint(object):
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

class NewTestVector(NewTestPoint):
    def init_new_vectors(self):
        self.init_new_points()

        self.vector_a = Vector(self.point_a, self.point_b)
        self.vector_b = Vector(self.point_b, self.point_a)

    def get_norm_vector_a(self):
        # point_c = self.point_b - self.point_a
        ## norm = point_c.x**2 + point_c.y**2
        return 10

    def get_vector_sub(self):
        x = -2
        y = 6
        return x, y
    def get_vector_sum(self):
        x = 0
        y = 0
        return x, y

    def get_vector_values_a(self):
        x = -1
        y = 3
        return x, y

    def get_vector_values_b(self):
        x , y = self.get_vector_values_a()
        x = -x
        y = -y
        return x, y