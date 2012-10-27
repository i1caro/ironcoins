from tests.main import MainTestClass
from pieces.models import Figure

class TestFigure(MainTestClass):
    source = Point(1,2)
    destination = Point(10,5)

    def get_figure(self):
        return Figure(name='Ogre', position=self.source)

    def test_creation(self):
        result = self.get_figure()
        assertEqual('Ogre(1,2)', str(result))

    def test_movement_down(self):
        result = self.get_figure().path_to(self.down)
        assertEqual('((0,0),(-1,0))', str(result))

    # def test_path(self):
    #     result = self.get_figure().path_to(destination)
    #     path = '((1,2),(2,3),(3,4),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5))'
    #     assertEqual(path, result)

class TestFigureCircularMovement(TestFigure):
    source = Point(2,2)
    left = Point(1,2)
    top_left = Point(1,3)
    top = Point(2,3)
    top_right = Point(3,3)
    right = Point(3,2)
    down_right = Point(3,1)
    down = Point(2,1)
    down_left = Point(1,1)


    def test_movement_left(self):
        result = self.get_figure().path_to(self.left)
        assertEqual('((2,2),(1,2))', str(result))

    def test_movement_top_left(self):
        result = self.get_figure().path_to(self.top_left)
        assertEqual('((2,2),(1,2),(1,3))', str(result))

    def test_movement_top(self):
        result = self.get_figure().path_to(self.top)
        assertEqual('((2,2),(2,3))', str(result))

    def test_movement_top_right(self):
        result = self.get_figure().path_to(self.top_right)
        assertEqual('((2,2),(2,3),(3,3))', str(result))

    def test_movement_right(self):
        result = self.get_figure().path_to(self.right)
        assertEqual('((2,2),(3,2))', str(result))

    def test_movement_down_right(self):
        result = self.get_figure().path_to(self.down_right)
        assertEqual('((2,2),(3,1))', str(result))

    def test_movement_down(self):
        result = self.get_figure().path_to(self.down)
        assertEqual('((2,2),(2,1))', str(result))

    def test_movement_down_left(self):
        result = self.get_figure().path_to(self.down_left)
        assertEqual('((2,2),(1,1))', str(result))

