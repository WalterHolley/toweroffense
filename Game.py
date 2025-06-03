'''
Game Rules:
Two players are required for the game.  The defender, and the attacker
A pre-set number of rounds is determined
The attacker will attempt to destroy all defenses, while the defender will work to maintain at least 1 structure.
After the rounds have concluded, If at lest 1 defending structure remains, the defender wins, otherwise the attacker wins

BEFORE ROUND:
The attacker chooses the unit(s) it wishes to send.  The defender decides  what unit(s) it uses to defend

EXECUTE ROUND:
The attacker's unit(s) move across the 'lane'.  When the unit(s) come in range they will attack one or the other.  Surviving units return to the
attacker if they reach the end of the lane

This is a comments test
'''

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




