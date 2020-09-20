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
        self.guest1 = Guest("Jimmy")
        self.guest2 = Guest("Billy")
        self.room.add_to_room(self.guest1)
        self.room.add_to_room(self.guest2)
        self.assertEqual([self.guest1, self.guest2], self.room.guest_list)

    def test_add_group_to_guestlist(self):
        self.group = ["Jimmy", "Billy", "Bimmy", "Karen"]
        self.room.add_group_to_room(self.group)
        self.assertEqual([self.group], self.room.guest_list)

    def test_check_guests_out(self):
        self.room.guest_list = ["Jimmy", "Billy", "Bimmy", "Karen"]
        self.assertEqual(0, self.room.check_out_of_room(self.room.guest_list))

    def test_add_songs_to_song_list(self):
        self.song1 = Song("Sunburnt through the glass, PREP")
        self.song2 = Song("Olha Pipa, Jorge Ben Jor")
        self.song3 = Song("Mali Mali, Disclosure")
        self.room.add_to_playlist(self.song1)
        self.room.add_to_playlist(self.song2)
        self.room.add_to_playlist(self.song3)
        self.assertEqual([self.song1, self.song2, self.song3], self.room.song_list)

