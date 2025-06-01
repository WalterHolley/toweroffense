from gameobjects import *

class Game(object):
    def __init__(self, P1: GameUnit, P2: GameUnit):
        P1.isMaster = True
        P2.isMaster = True

        self.Player = P1
        self.opponent = P2
    
    def moveUnits(attackUnits):
        pass
    def attackUnits(gameUnits):
        pass




