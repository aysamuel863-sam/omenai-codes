class Character:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Level:  {self.level}")
        
    def level_up(self):    
        self.level += 1
        print(f"{self.name} is leveled up!")    
        print(f"{self.name} is now in level {self.level}.")

    def take_damage(self, damage):
            self.health -= damage
    
            if self.health < 0:
                self.health = 0
            print(f"{self.name} took {damage}, damage!")
            print(f"{self.name} has {self.health} left")

    def heal(self):
        self.health += 20
        print(f"{self.name} healed!")
        print(f"{self.name} now has {self.health} health.")

player = Character("Shadow", 100, 1)

player.introduce()
player.level_up()
player.take_damage(40)
player.heal()
