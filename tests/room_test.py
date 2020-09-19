import unittest

from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def test_room_has_name(self):
        self.room = Room("Smashie's Palace")
        self.assertEqual("Smashie's Palace", self.room.room_name)

    def test_check_guest_into_room(self):
        self.guest_list = ["Jimmy", "June", "Suzie", "Bimble", "Spot"]
        self.assertEqual(["Jimmy", "June", "Suzie", "Bimble", "Spot"], self.room.check_in)

    
