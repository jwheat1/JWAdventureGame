import random

# -------- CLASSES --------
class Player:
    def __init__(self, name, health, equipment, location):
        self.name = name
        self.health = health
        self.equipment = equipment
        self.location = location

    def get_health(self):
        return self.health
    
    def update_health(self, value):
        self.health += value

    def get_equipment(self):
        return self.equipment

    def add_equipment(self, item):
        self.equipment.append(item)


class Creature:
    def __init__(self, species, health, behavior):
        self.species = species
        self.health = health
        self.behavior = behavior
    
    def get_health(self):
        return self.health

    def update_health(self, damage):
        self.health -= damage


class GameState:
    def __init__(self):
        self.hasDataLog = False
        self.hasCreatureData = False
        self.hasControlRoomKey = False
        self.hasBackupPowerCell = False
        self.current_chapter = 1
        self.game_won = False
        self.game_ended = False

# Initialize objects
player = Player("Engineer", 100, [], "Docking Bay")
creature = Creature("Unknown Alien", 50, "Hostile")