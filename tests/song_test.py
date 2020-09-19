import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def test_song_has_name(self):
        self.song = Song("Cheapest Flight", "PREP")
        self.assertEqual("Cheapest Flight", self.song.title)
        
    def test_song_has_artist(self):
        self.song = Song("Cheapest Flight", "PREP")
        self.assertEqual("PREP", self.song.artist)

