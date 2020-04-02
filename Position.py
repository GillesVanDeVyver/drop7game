# Positions identify individual cells on game boards.

def is_proper_position(dimension, position):
    """
        Check whether the given position is a proper position for any board
        with the given dimension.
        - The given position must be a tuple of length 2 whose elements are both
          natural numbers.
        - The first element identifies the column. It may not exceed the given
          dimension.
        - The second element identifies the row. It may not exceed the given
          dimension incremented with 1 (taking into account the overflow position)
        - The function returns True if the position is indeed a proper  position, False otherwise.
        - The function uses the helper function is_natural_number. (see POSITION HELPER FUNCTIONS below)
        ASSUMPTIONS
        - None
    """

    if not isinstance(position, tuple) or \
        len(position) != 2 or \
        not is_natural_number(position[0]) or \
        position[0] > dimension or \
        not is_natural_number(position[1]) or \
        position[1] > dimension + 1:

        return False

    return True


def is_overflow_position(dimension, position):
    """
        Check whether the given position is an overflow position for any board
        with the given dimension.
        - True if and only if the position is in the overflow row of the given board.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
    """

    if position[1] == dimension + 1:
        return True

    return False


def left(dimension, position):
    """
        Return the position on any board with the given dimension immediately to
        the left of the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
    """

    if position[0] == 1:
        return None

    return position[0]-1, position[1]


def right(dimension, position):
    """
       Return the position on any board with the given dimension immediately to
       the right of the given position.
       - None is returned if the generated position is outside the boundaries of
         a board with the given dimension.
       ASSUMPTIONS
       - The given position is a proper position for any board with the
         given dimension.
     """

    if position[0] == dimension:
        return None

    return position[0]+1, position[1]


def up(dimension, position):
    """
        Return the position on any board with the given dimension immediately
        above the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """

    if position[1] == dimension+1:
        return None

    return position[0], position[1]+1


def down(dimension, position):
    """
        Return the position on any board with the given dimension immediately
        below the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """

    if position[1] == 1:
        return None

    return position[0], position[1]-1


def next(dimension, position):
    """
        Return the position on any board with the given dimension next to the
        given position.
        - If the given position is not at the end of a row, the resulting position
          is immediately to the right of the given position.
        - If the given position is at the end of a row, the resulting position is
          the leftmost position of the row above. If that next row does not exist,
          None is returned.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """

    if position[0] != dimension:
        return right(dimension, position)

    elif position[1] != dimension + 1:
        return up(dimension, (1, position[1]))

    else:
        return None


def get_all_adjacent_positions(dimension, positions):
    """
        Return a mutable set of all positions adjacent to at least one of the positions
        in the given collection of positions and within the boundaries of any board
        with the given dimension.
        - If no positions are given, there are no adjacent positions.
        ASSUMPTIONS
        - Each position in the given collection of positions is a proper position
          for any board with the given dimension.
    """

    adjacent_positions = set()
    positions = tuple(positions)

    if positions == ():
        return adjacent_positions

    for i in positions:
        set.add(adjacent_positions, left(dimension, i))
        set.add(adjacent_positions, right(dimension, i))
        set.add(adjacent_positions, up(dimension, i))
        set.add(adjacent_positions, down(dimension, i))
        adjacent_positions = set.difference(adjacent_positions, {None})     # If one of the fucntions
        # left,right,up or down returns None, this must be removed from the list.

    return adjacent_positions

### POSITION HELPER FUNCTIONS ###

def is_natural_number(number):
    """
        Check whether the given number is a natural number.
        - Returns True if the given number is a
          natural number, False otherwise.
        - 0 is not considered a natural number.
        - The function also returns False if the given number
          is not an integer.
    """

    if isinstance(number, int) and number > 0:
        return True

    return False