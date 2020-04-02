import random

# Disks can be stored on the game board. They have a state
# and a number.
#  - Disks are mutable things. More in particular, it must be
#    possible to change the state of a disk.

# Enumeration of the possible states of a disk.
VISIBLE = 10
CRACKED = 20
WRAPPED = 30
All_states = (VISIBLE, CRACKED, WRAPPED)        # Additional self-defined states should be in this list when used.


def is_proper_disk(dimension, disk):
    """
       Check whether the given disk is a proper disk for any board with
       the given dimension.
       - The state of the given disk must be one of the values VISIBLE,
         WRAPPED, CRACKED or some additional self-defined state.
       - The value of the given disk must be a positive integer number
         that does not exceed the dimension of the given board.
       - Disks are represented as lists with 2 elements: [state, value]
         or as None is case the 'disk' represents a empty space on the board. (see init_disk)
       ASSUMPTIONS
       - None
    """

    if disk[0] not in All_states:
        return False

    if not isinstance(disk[1], int) or disk[1] > dimension:
        return False

    return True


def init_disk(state, value):
    """
       Return a new disk with given state and given value.
       - Disks are represented as lists with 2 elements: [state, value]
         or as None is case the 'disk' represents a empty space on the board.
       ASSUMPTIONS
       - None
    """

    disk = [state, value]

    return disk


def get_random_disk(dimension, possible_states):
    """
       Return a random disk for a board with the given dimension with
       a state that belongs to the collection of possible states.
       ASSUMPTIONS
       - The given dimension is positive.
       - The given collection of possible states is not empty and contains
         only elements VISIBLE, WRAPPED and/or CRACKED
    """

    value = random.randint(1, dimension)
    state = random.choice(tuple(possible_states))

    return [state, value]


def set_state(disk, state):
    """
        Set the state of the given disk to the given state.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """

    disk[0] = state

    return disk


def get_state(disk):
    """
        Return the state of the given disk.
        - If the given disk is None (empty place on board), the function returns None.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """

    if disk is None:
        return

    return disk[0]


def set_value(disk, value):
    """
        Set the value of the given disk to the given value.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """

    disk[1] = value


def get_value(disk):
    """
        Return the value of the given disk.
        - If the given disk is None (empty place on board), the function returns None.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """

    if disk is None:
         return

    return disk[1]


def get_disk_copy(disk):
    """
        Return a new disk whose state and value are identical to the
        state and value of the given disk.
        - If the given disk is None (empty place on board), the function returns None.
        ASSUMPTIONS
        - The given disk is a proper disk for any board with a dimension at
          least equal to the value of the given disk.
    """

    if disk is None:
        return

    return disk[:]