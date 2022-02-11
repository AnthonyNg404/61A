class Bee(Insect):
    """A Bee moves from place to place, following exits and stinging ants."""

    name = 'Bee'
    damage = 1
    is_watersafe = True
    is_scary = False
    # OVERRIDE CLASS ATTRIBUTES HERE


    def sting(self, ant):
        """Attack an ANT, reducing its armor by 1."""
        ant.reduce_armor(self.damage)

    def move_to(self, place):
        """Move from the Bee's current Place to a new PLACE."""
        self.place.remove_insect(self)
        place.add_insect(self)

    def blocked(self):
        """Return True if this Bee cannot advance to the next Place."""
        # Phase 4: Special handling for NinjaAnt
        # BEGIN Problem 7
        return self.place.ant is not None and self.place.ant.blocks_path is True
        # END Problem 7

    def action(self, colony):
        """A Bee's action stings the Ant that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.

        colony -- The AntColony, used to access game state information.
        """
        destination = self.place.exit
        reversed_destination = self.place.entrance
        # Extra credit: Special handling for bee direction
        # BEGIN EC

        # END EC
        if self.blocked():
            self.sting(self.place.ant)
        elif self.armor > 0 and destination is not None:
            self.move_to(destination)


class ThrowerAnt(Ant):
    """ThrowerAnt throws a leaf each turn at the nearest Bee in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    food_cost = 3
    min_range = 0
    max_range = 0
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE

    def nearest_bee(self, beehive):
        """Return the nearest Bee in a Place that is not the HIVE, connected to
        the ThrowerAnt's Place by following entrances.

        This method returns None if there is no such Bee (or none in range).
        """
        # BEGIN Problem 3 and 4
        current_place = self.place
        if self.min_range == 0 and self.max_range == 0:
            while current_place is not beehive:
                if current_place.bees:
                    return random_or_none(current_place.bees)
                else:
                    current_place = current_place.entrance
            return None
        elif self.min_range > 0:
            for i in range(self.min_range):
                current_place = current_place.entrance
                if current_place is beehive:
                    return None
            while current_place is not beehive:
                if current_place.bees:
                    return random_or_none(current_place.bees)
                else:
                    current_place = current_place.entrance
            return None
        else:
            current_range = 0
            while current_place is not beehive:
                if current_range > self.max_range:
                    return None
                elif current_place.bees:
                    return random_or_none(current_place.bees)
                else:
                    current_place = current_place.entrance
                    current_range += 1
            return None
        # END Problem 3 and 4

    def throw_at(self, target):
        """Throw a leaf at the TARGET Bee, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a leaf at the nearest Bee in range."""
        self.throw_at(self.nearest_bee(colony.beehive))



def make_slow(action, bee):
    """Return a new action method that calls ACTION every other turn.

    action -- An action method of some Bee
    """
    # BEGIN Problem EC
    if colony.time % 2 == 1:
        return None
    else:
        bee.action(colony)
    # END Problem EC

def make_scare(action, bee):
    """Return a new action method that makes the bee go backwards.

    action -- An action method of some Bee
    """
    # BEGIN Problem EC
    bee.is_scary = True
    if self.place is beehive:
        return None
    elif self.armor > 0:
        bee.action.move_to(reversed_destination)
    # END Problem EC

def apply_effect(effect, bee, duration):
    """Apply a status effect to a BEE that lasts for DURATION turns."""
    # BEGIN Problem EC
    while duration > 0:
        if effect == make_slow:
            bee.action = effect(action, bee)
            if colony.time % 2 == 0:
                duration -= 1
        elif effect == make_scare:
            bee.action = effect(action, bee)
            duration -= 1

    # END Problem EC


class SlowThrower(ThrowerAnt):
    """ThrowerAnt that causes Slow on Bees."""

    name = 'Slow'
    food_cost = 4
    # BEGIN Problem EC
    implemented = True   # Change to True to view in the GUI
    # END Problem EC

    def throw_at(self, target):
        if target:
            apply_effect(make_slow, target, 3)


class ScaryThrower(ThrowerAnt):
    """ThrowerAnt that intimidates Bees, making them back away instead of advancing."""

    name = 'Scary'
    food_cost = 6
    # BEGIN Problem EC
    implemented = True   # Change to True to view in the GUI
    # END Problem EC

    def throw_at(self, target):
        # BEGIN Problem EC
        if target and not target.is_scary:
            apply_effect(make_scare, target, 2)
        # END Problem EC


