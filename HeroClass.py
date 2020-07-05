import time
class Hero:
    def __init__(self, name):
        self.name = name
        self.power = {}
        self.health = 100
        self.enemy = None
        self.color = None
        self.wins = 0
        self.ai = False
    def setEnemy(self, enemy):
        self.enemy = enemy
    def setPower(self, power, damage, prob):
        self.power[power] = (damage, prob)
    def attack(self, move):
        if self.enemy == None:
            print("There is no enemy to attack.")
        else:
            damage = self.power[move][0]
            self.enemy.health -= damage









