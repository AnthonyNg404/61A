This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

	>>> from ants import *

	Case 1
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> colony = AntColony(None, beehive, ant_types(), layout, dimensions)
    >>> # Testing Slow
    >>> slow = SlowThrower()
    >>> bee = Bee(3)
    >>> colony.places["tunnel_0_0"].add_insect(slow)
    >>> colony.places["tunnel_0_4"].add_insect(bee)
    >>> slow.action(colony)
    >>> colony.time = 1
    >>> bee.action(colony)
    >>> bee.place.name # SlowThrower should cause slowness on odd turns
    'tunnel_0_4'
    >>> colony.time += 1
    >>> bee.action(colony)
    >>> bee.place.name # SlowThrower should cause slowness on odd turns
    'tunnel_0_3'
    >>> for _ in range(3):
    ...    colony.time += 1
    ...    bee.action(colony)
    >>> bee.place.name
    'tunnel_0_2'



Suite 2
    >>> from ants import *

    Case 1
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> colony = AntColony(None, beehive, ant_types(), layout, dimensions)
    >>> # Testing Scare
    >>> scary = ScaryThrower()
    >>> bee = Bee(3)
    >>> colony.places["tunnel_0_0"].add_insect(scary)
    >>> colony.places["tunnel_0_4"].add_insect(bee)
    >>> scary.action(colony)
    >>> bee.action(colony)
    >>> bee.move_back