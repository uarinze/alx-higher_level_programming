'''#!/usr/bin/python3'''

import random
import math

class Warrior:

    def __init__(self, name="Warrior", health="0", attkMax="0", blockMax="0"):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)
        return attkAmt


    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)
        return blockAmt

class Battle:

    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()
        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2WarriorB
        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage2WarriorB))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))
        if warriorB.health <= 0:
            print("{} has dies and {} is victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():
    maximus = Warrior("Maximus", 50, 20, 10)
    galaxon = Warrior("Galaxon", 50, 20, 10)
    battle = Battle()
    battle.startFight(maximus, galaxon)

main()
