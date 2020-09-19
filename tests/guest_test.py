import unittest

from src.room import Room
from src.guest import Guest
from src.song import song


class KaraokeGuestTest(unittest.TestCase):

    def setUp(self):
        guest_1 = Guest("Jimmy", 22, 100)
        guest_2 = Guest("June", 19, 150)

    def test_guest_has_name(self):
        self.assertEqual("Jimmy", self.guest_1.name)