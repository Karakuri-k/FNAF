import random as rd

class Animatronic:
    def __init__(self, path:list) -> None:
        self.path = path
        self.position = 0
        self.see:bool = False

    def move(self):
        #legg inn timer
        if self.position == len(self.path):
            self.position -=1
        elif self.position == 0:
            self.position +=1
        else:
            a = rd.randint(-1, 1)
            self.position += a

    def seePlayer(self, door):
        if self.position == len(self.path) and door.locked == False:
            self.see = True
        else: 
            self.see = False

class Light:
    def __init__(self) -> None:
        self.light = False

    def onOff(self):
        if self.light == False:
            self.light = True
        else:
            self.light = False

class Door:
    def __init__(self) -> None:
        self.locked:bool = False

    def lockDoor(self):
        if self.locked == False:
            self.locked = True
        else:
            self.locked = False