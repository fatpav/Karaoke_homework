import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        
        self.guest_1 = Guest("Jimmy")
        self.guest_2 = Guest("June")

    def test_guest_has_name(self):
        self.assertEqual("Jimmy", self.guest_1.name)
        self.assertEqual("June", self.guest_2.name)
    
    # def test_guest_has_age(self):
    #     self.assertEqual(22, self.guest_1.age)
    #     self.assertEqual(19, self.guest_2.age)

    # def test_guest_has_cash(self):
    #     self.assertEqual(100, self.guest_1.cash)
    #     self.assertEqual(150, self.guest_2.cash)

