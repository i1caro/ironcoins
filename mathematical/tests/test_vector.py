from mathematical.tests.main import MainTestClass
from mathematical.tests.object_init import NewTestVector
from mathematical.trigonometry import Point
from mathematical.trigonometry import Vector


# class TestVector(MainTestClass, NewTestVector):
#     def test_norm(self):
#         self.init_new_vectors()
#         self.assertEqual(self.vector_a.norm(), self.get_norm_vector_a())

#     def test_equality_norm(self):
#         self.init_new_vectors()
#         self.assertEqual(self.vector_a.norm(), self.vector_b.norm())

#     def test_sum(self):
#         self.init_new_vectors()
#         vector_c = self.vector_a + self.vector_b
#         x, y = self.get_vector_sum()
#         self.assertEqual(vector_c.x , x)
#         self.assertEqual(vector_c.y , y)

#     def test_sub(self):
#         self.init_new_vectors()
#         vector_c = self.vector_a - self.vector_b
#         x, y = self.get_vector_sub()
#         self.assertEqual(vector_c.x , x)
#         self.assertEqual(vector_c.y , y)