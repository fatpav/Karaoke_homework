class Room:
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.song_list = []

    def add_to_room(self, guest):
        self.guest_list.append(guest)

    def add_group_to_room(self, group):
        self.guest_list.append(group)
        return self.guest_list

    def check_out_of_room(self, guests):
        self.guest_list *= 0
        return len(self.guest_list)

    def add_to_playlist(self, song):
        self.song_list.append(song)
        return self.song_list
        
    

    

        
        