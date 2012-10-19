from tests.main import MainTestClass
from mathematical.tests.object_init import NewTestPoint

class TestPoint(MainTestClass, NewTestPoint):

    def test_sum(self):
        self.init_new_points()
        point_c = self.point_a + self.point_b
        x ,y = self.get_sum()

        self.assertEqual(point_c.x, x)
        self.assertEqual(point_c.y, y)

    def test_sub(self):
        self.init_new_points()
        point_c = self.point_a + self.point_b
        x ,y = self.get_sum()

        self.assertEqual(point_c.x, x)
        self.assertEqual(point_c.y, y)

    def test_equality(self):
        self.init_new_points()
        point_c = self.point_a
        
        self.assertEqual(point_c.x, self.point_a.x)
        self.assertEqual(point_c.y, self.point_a.y)
