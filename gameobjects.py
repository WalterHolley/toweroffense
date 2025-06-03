
BASE_AT = 1000

class GameUnit(object):

    def __init__(self, speed, attack, hp, crit):
        self.speed = speed
        self.attack = attack
        self.crit = crit
        self.hp = hp
        self.isMaster = False

class AttackUnit(GameUnit):
    def __init__(self, speed, attack, hp, crit, owner: GameUnit):
        super().__init__(speed, attack, hp, crit)
        self.owner = owner
   
    def isDead(self):
        if self.hp == 0:
            return True
        return False

    def unitAT(self):
       return BASE_AT - (self.speed * 100)

class StructureUnit(GameUnit):
    def __init__(self, speed, attack, hp, crit, owner: GameUnit):
        super().__init__(speed, attack, hp, crit)
        self.owner = owner






