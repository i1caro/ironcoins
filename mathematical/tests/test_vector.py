from mathematical.tests.main import MainTestClass
from mathematical.trigonometry import Point
from mathematical.trigonometry import Vector

class TestVector(MainTestClass):
    vector_a = Vector(Point(5,7), Point(4,10))
    vector_b = Vector(Point(10,2), Point(4,7))

    def test_norm(self):
        self.assertEqual(10, self.vector_a.norm)

    def test_creation_b(self):
        self.assertEqual('(-6,5)', str(self.vector_b))

    def test_creation_a(self):
        self.assertEqual('(-1,3)', str(self.vector_a))

    def test_sum(self):
        result = self.vector_a + self.vector_b
        self.assertEqual('(-7,8)', str(result))
        
    def test_sub(self):
        result = self.vector_a - self.vector_b
        self.assertEqual('(5,-2)', str(result))


        