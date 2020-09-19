import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Smashie's Palace")
        
    def test_room_has_name(self):
        self.assertEqual("Smashie's Palace", self.room.name)

    def test_guest_can_join_room(self):
        self.guest1 = "Jimmy"
        self.guest2 = "Billy"
        self.room.add_to_room(self.guest1)
        self.room.add_to_room(self.guest2)
        self.assertEqual(["Jimmy", "Billy"], self.room.guest_list)

    def check_guests_out