class Door:
    def __init__(self,is_opened):
        self.is_open=is_opened

    def open_door(self):
        self.is_open=True

    def close_door(self):
        self.is_open=False

class BlockedDoor(Door):
    def open_door(self):
        self.is_open=False

door1=BlockedDoor(True)
    


