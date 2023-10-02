# Object-Oriented Programming

class Player:
    # Attributes
    name = None
    health = None
    defense = None
    attack = None
    armor = None

    # Methods
    def __init__(self, name, health):
        self.health = 100
        self.defense = 50
        self.attack = 10
        self.name = name
    
    def getHealth(self):
        return self.health

    def increaseHealth(self, amount_of_health):
        self.health += amount_of_health
        print(f"Player increased health by {self.health}!")
    
    def increaseAttack(self, amount_of_attack):
        self.attack += amount_of_attack
    
    @classmethod
    def instanciate_object_health(cls):
        return cls.health

player1 = Player()