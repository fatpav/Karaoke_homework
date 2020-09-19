class Room:
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.song_list = []

    def add_to_room(self, guest):
        self.guest_list.append(guest)
        return self.guest_list
    

    

        
        