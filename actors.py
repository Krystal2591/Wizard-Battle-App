import random

class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def get_defensive_roll(self):
        return random.randint(1,12)*self.level


class Wizard(Creature):

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(self.name, creature.name))
        my_roll=self.get_defensive_roll()
        creature_roll= creature.get_defensive_roll()

        print ('Gandolf scores {}'.format(my_roll))
        print ('{} scores {}'.format(creature.name, creature_roll))

        if my_roll>=creature_roll:
            print ('Gandolf has defeated {}'.format(creature.name))
            return True
        else:
            print ('Gandolf, the wizard has been defeated.')
            return False





class Small_Animal(Creature):
    def get_defensive_roll(self):
        base_roll=super().get_defensive_roll()
        return base_roll/2


class Dragon(Creature):
    def __init__(self, name, level, scale_thickness,breaths_fire):
        super().__init__(name, level)
        self.scale_thickness=scale_thickness
        self.breaths_fire=breaths_fire

    def get_defensive_roll(self):
        base_roll=super().get_defensive_roll()
        fire_modifier=5 if self.breaths_fire else 1
        scale_modifier=self.scale_thickness/10

        return base_roll*fire_modifier*scale_modifier


class Predator(Creature):
    pass