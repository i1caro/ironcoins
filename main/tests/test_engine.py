from tests.main import MainTestClass
from main.engine import Action

class TestAction(MainTestClass):
    # def setUp(self):
    #     super(MainTestClass, self).setUp()

    def test_action_initiative(self):
        a = Action(4)
        self.assertEqual(4, a.initiative)

    def test_action_equality(self):
        a = Action(4)
        b = Action(4)
        self.assertEqual(b, a)

    def test_action_greater(self):
        a = Action(4)
        b = Action(5)
        self.assertGreater(b, a)

class TestMovement(MainTestClass):
    pass


        