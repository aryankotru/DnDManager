

class Character:

    def __init__(self):
        
        print("executing")
        #self.stats = ['Strength', 'Intelligence', 'Charisma', 'Perception', 'Luck', 'Health', 'Agility']]
        self.strength = 0
        self.intelligence = 0
        self.charisma = 0
        self.perception = 0
        self.luck = 0
        self.agility = 0
        self.health = 100
        self.get_status()

    
    def type(self):
        type = ['Swordsman', 'Magician', 'Archer']

    def playerstats(self):
        print("Enter strength:")
        self.strength = int(input())
        print("Enter intelligence:")
        self.intelligence = int(input())
        print("Enter charisma:")
        self.charisma = int(input())
        print("Enter perception:")
        self.perception = int(input())
        print("Enter luck:")
        self.luck = int(input())
        print("Enter agility:")
        self.agility = int(input())

    
    def attack(self, target):
        target.hp -= self.ap

    def get_status(self):
        self.name = input("Enter your character's name:")
        #print(self.name)
        return self.name + ' ' #+ str(self.hp)
    
c = Character()
print("executing main")
c.get_status()