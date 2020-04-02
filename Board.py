import Disk
import Position
import copy

# Boards are square areas of N rows and N columns.=
#     - Rows and columns in boards are numbered starting from 1.


def is_proper_board(board):
    """
        Check whether the given board is a proper board. The function
        returns true iff all the conditions below are satisfied:
        - The given board may not be None, and its dimension
          must be a natural number.
        - Each cell of the given board either stores nothing (None),
          or it stores a proper disk for the given board.
        - Boards are represented as lists. (see init_board)
        ASSUMPTIONS
        - None
    """

    dimension_board = dimension(board)

    if not dimension_board:
        return False

    for column in range(len(board)):

        for row in range(len(board)+1):

            disk = get_disk_at(board,(column+1,row+1))

            if disk is not None and not Disk.is_proper_disk(dimension_board,disk):
                return False

    return True


def is_playable_board(board):
    """
        Check whether the given board is a playable board. The function
        returns true iff all the conditions below are satisfied:
        - The given board is a proper board.
        - If a cell stores a disk, all cells below also store
          a disk (i.e. there are no gaps in columns).
        - The same disk is not stored at several positions on the given board.
        - Boards are represented as lists. (see init_board)
        - The function uses the helper function disk_on_several_positions.(see BOARD HELPER FUNCTIONS below)
        ASSUMPTIONS
        - None
    """

    if not is_proper_board(board):
        return False

    for column in range(len(board)):

        gap = False

        for row in range(len(board)+1):
            disk = get_disk_at(board,(column + 1, row + 1))

            if disk is not None and gap:
                return False

            if disk is None:
                gap = True

            elif disk_on_several_positions(disk,board):
                return False

    return True


def init_board(dimension, given_disks=()):
    """
        Return a new board with given dimension and filled with the given disks.

        - The collection of given disks is a sequence. The element at position I
          in that sequence specifies the disks to be loaded on column I+1 of the
          new board.
        - If there is no matching element for a column, no disks are loaded on
          that column.
        - Boards are represented as lists. Each element of this list represents
          a column on the board. Each column is a list with the same length as
          the dimension of the board containing the disks stored in the column.
        ASSUMPTIONS
        - The given dimension is a positive integer number.
        - The number of elements in the sequence of given disks is between 0
          and the given dimension.
        - Each element of the given sequence of disks is a sequence of
          disks for the new board. The length of each sequence of disks
          is less than or equal to the given dimension incremented with 1.
          Each disk must be a proper disk for the given board.
        NOTE
        - Notice that the resulting board will be a proper board, but not
          necessarily a playable board. Notice also that some disks on the board
          might satisfy the conditions to explode.
    """

    board = [[None]*(dimension+1) for k in range(dimension)]

    for column in range(len(given_disks)):

        for row in range(len(given_disks[column])):
            board[column][row] = given_disks[column][row]

    return board


def get_board_copy(board):
    """
      Return a full copy of the given board.
      - The resulting copy contains copies of the disks stored
         on the original board.
      ASSUMPTIONS
      - The given board is a proper board.
    """

    return copy.deepcopy(board)


def dimension(board):
    """
        Return the dimension of the given board.
        - The dimension of a square board is its number of rows or equivalently
          its number of columns.
        - The function returns None if no dimension can be obtained from the given
          board. This is for instance the case if a string, a number, ... is passed
          instead of a board.
        ASSUMPTIONS
        - None (we must be able to use this function at times the thing that
          is given to us is not necessarily a proper board, e.g. in the function
          is_proper_board itself)
    """

    if not isinstance(board,list):
        return None

    elif len(board) +1 != len(board[0]):        # Taking into account he overflow position.
        return None

    else:
        return len(board)


def get_disk_at(board, position):
    """
        Return the disk at the given position on the given board.
        - None is returned if there is no disk at the given position.
        - The function also returns None if no disk can be obtained from the given
          board at the given position. This is for instance the case if a string,
          a number, ... is passed instead of a board or a position, if the given
          position is outside the boundaries of the given board, ...
        ASSUMPTIONS
        - None (same remark as for the function dimension)
     """

    dimension_board = dimension(board)

    if not isinstance(board,list) or not isinstance(position,(list,tuple)) or \
        position[0] > dimension_board or position[1] > (dimension_board+1):
        return

    return board[position[0]-1][position[1]-1]


def set_disk_at(board, position, disk):
    """
        Fill the cell at the given position on the given board with the given disk.
        - The disk nor any other disk will yet explode, even if the conditions
          for having an explosion are satisfied.
        - The given disk may be None, in which case the disk, if any, at the given
          position is removed from the given board, WITHOUT disks at higher positions
          in the column dropping down one position.
        ASSUMPTIONS
        - The given board is a proper board, the given position is a proper
          proper position for the given board and the given disk is a proper
          disk for the given board.
    """

    board[position[0]-1][position[1]-1]=disk


def has_disk_at(board, position):
    """
        Check whether a disk is stored at the given position on the given board.
        - The function returns false if no disk can be obtained from the given
          board at the given position.
        ASSUMPTIONS
        - The given board is a proper board and the given position is a
          proper position for that board.
    """

    if get_disk_at(board,position) is None:
        return False

    return True


def is_full_column(board, column):
    """
       Check whether the non-overflow part of the given column on the given board
       is completely filled with disks.
       - The overflow cell of a full column may also contain a disk, but it may
         also be empty.
        ASSUMPTIONS
        - The given board is a proper board, and the given column is a proper column
          for that board.
    """

    for row in range(dimension(board)):

        if get_disk_at(board, (column, row+1)) is None:
            return False

    return True


def is_full(board):
    """
       Check whether the non-overflow part of the  given board is completely
       filled with disks.
        - Returns False if there is at least one disk in the column None.(Not
          taking into account the overflow position)
        ASSUMPTIONS
        - The given board is a proper board.
    """

    for column in range(len(board)):

        if not is_full_column(board,column+1):
            return False

    return True

def can_accept_disk(board):
    """
        Check whether the given board can accept an additional disk.
        - True if and only if (1) all overflow cells of the given board are free,
          and (2) at least one of the cells in the non-overflow portion of the
          given board is free.
        ASSUMPTIONS
        - The given board is a proper board.

    """

    if is_full(board):
        return False

    for column in range(len(board)):

        if board[column][dimension(board)] is not None:     # Checks whether the overflow row doesn't contain a disk.
            return False

    return True


def add_disk_on_column(board, disk, column):
    """
        Add the given disk on top of the given column of the given board.
        - The disk is registered at the lowest free position in the given column.
          Nothing happens if the given column is completely filled, including the
          overflow cell of that column.
        - The disk nor any other disk will yet explode, even if the conditions for
          having an explosion are satisfied.
        ASSUMPTIONS
        - The given board is a proper board, the given column is a proper column
          for the given board, and the given disk is a proper disk for the given board.
    """

    for row in range(dimension(board)+1):

        if get_disk_at(board, (column, row+1)) is None:
            set_disk_at(board,(column,row+1),disk)
            return



def inject_disk_in_column(board, disk, column):
    """
        Inject the given disk at the bottom of the given column of the given board.
        - The disk is registered in the bottom cell of the given column, i.e., in the
          cell at row 1.
        - All disks already in the given column are shifted up one position.
        ASSUMPTIONS
        - The given board is a proper board, the given column is a proper column
          for that board whose overflow cell is free, and the given disk is a
          proper disk for the given board.
    """

    new_column = [None] + board[column-1][:-1]      # Creates a new column with a free space at the bottom.
    board[column-1] = new_column
    set_disk_at(board,(column,1),disk)


def inject_bottom_row_wrapped_disks(board):
    """
        Insert a bottom row of wrapped disks in the given board.
        - All disks already in the board are shifted up one position.
        - No disk on the given board will explode yet, even if the conditions
          for having an explosion are satisfied.
        ASSUMPTIONS
        - The given board is a playable board that can accept a disk.
    """

    for column in range(len(board)):

        disk = Disk.get_random_disk(dimension(board),(Disk.WRAPPED,))
        inject_disk_in_column(board, disk, column)


def remove_disk_at(board, position):
    """
        Remove the disk at the given position from the given board.
        - All disks above the removed disk drop one position down.
        - Nothing happens if no disk is stored at the given position.
        - No disk will explode yet, even if the conditions for having an
          explosion are satisfied.
        ASSUMPTIONS
        - The given board is a proper board, and the given position is
          a proper position for that board.
        NOTE
        - This function must be implemented in a RECURSIVE way.
    """

    disk = get_disk_at(board,position)

    if disk is None:
        return

    if position[1] == dimension(board)+1:
        board[position[0] - 1][position[1] - 1] = None

        return

    board[position[0]-1][position[1]-1] = board[position[0]-1][position[1]]     # The disk above the removed disk drops.

    return remove_disk_at(board,(position[0], position[1]+1))


def get_length_vertical_chain(board, position,start_row = None):
    """
        Return the length of the vertical chain of disks involving the given
        position. Zero is returned if no disk is stored at the given position.
        ASSUMPTIONS
        - The given board is a playable board and the given position is a
          proper position for the given
          board.
        - If the given board does not store a disk on the given position, the function returns 0.
        NOTE
        - This function must be implemented in a RECURSIVE way.

    """

    if start_row is None:
        start_row = 0

    if get_disk_at(board, position) is None:
        return 0

    if start_row > dimension(board) or not get_disk_at(board,(position[0], start_row+1)):
        return 0

    start_row += 1

    return 1 + get_length_vertical_chain(board, position, start_row)


def get_length_horizontal_chain(board, position):
    """
        Return the length of the horizontal chain of disks involving the given
        position. Zero is returned if no disk is stored at the given position.
        ASSUMPTIONS
        - The given board is a proper board and the given position is a
          proper position for the given board.
        - The function uses the helper functions chain_left and chain_right.(see BOARD HELPER FUNCTIONS below)
    """

    if get_disk_at(board, position) is None:
        return 0

    return 1+ chain_left(board, position,position[0]-2) + chain_right(board, position,position[0])


def is_to_explode(board, position):
    """
        Return a boolean indicating whether the disk, if any, at the given
        position on the given board satisfies the conditions to explode.
        - True if and only if (1) the disk at the given position is visible, and
          (2) the number of the disk is equal to the length of the horizontal chain
          and/or the vertical chain involving that position.
        ASSUMPTIONS
        - The given board is a proper board and the given position is a
          proper position for the given board.
    """
    disk = get_disk_at(board, position)

    if Disk.get_state(disk) != Disk.VISIBLE:
        return False

    if Disk.get_value(disk) == get_length_horizontal_chain(board, position) or\
        Disk.get_value(disk) == get_length_vertical_chain(board, position):

        return True

    return False


def get_all_positions_to_explode(board,start_pos=(1,1)):
    """
        Return a frozen set of all positions on the given board that
        have a disk that satisfies the conditions to explode, starting
        from the given position and proceeding to the top of the board
        using the next function.
        - The function returns the empty set if the given start position
          is None.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given start position is either None or it is a proper position
          for the given board.
        NOTE
        - The second parameter should not be included in the code that
          is given to the students. They must learn to extend functions
          with extra parameters with a default value. The documentation
          of the function must be changed in view of that.
    """

    if start_pos is None:
        return frozenset ()

    if is_to_explode(board, start_pos):
        result = frozenset(((start_pos),)) | \
        get_all_positions_to_explode(board, (Position.next(dimension(board),start_pos)))


    else:
        result = get_all_positions_to_explode(board, (Position.next(dimension(board),start_pos)))

    return result


def crack_disks_at(board, positions):
    """
        Crack all disks at the given positions on the given board.
        - Wrapped disks will become cracked, and cracked disks will become
          visible.
        - Some positions may not contain any disk, or may contain non-crackable
          disks.
        ASSUMPTIONS
        - The given board is a proper board, and each of the given positions
          is a proper position for the given board.
    """
    for position in positions:

        disk = get_disk_at(board,position)

        if Disk.get_state(disk) == Disk.CRACKED:
            Disk.set_state(disk, Disk.VISIBLE)

        elif Disk.get_state(disk) == Disk.WRAPPED:
            Disk.set_state(disk, Disk.CRACKED)


def remove_all_disks_at(board, positions):
    """
        Remove all disks at the given positions on the given board.
        - All disks on top of disks that are removed drop down.
        - Positions in the given collection of positions at which no disk
          is stored, are ignored.
        ASSUMPTIONS
        - The given board is a proper board, and each of the given positions
          is a proper position for the given board.
    """

    for current_row in range(dimension(board)+1,0,-1):      # The positions higher in the board must be removed first.

        for position_to_remove in positions:

            if position_to_remove[1] == current_row:
                remove_disk_at(board, position_to_remove)


### BOARD HELPER FUNCTIONS ###

def disk_on_several_positions(disk,board):
    """
        Check whether the given disk is stored at several positions on the given board.
        - Returns True if the given disk appears more than once in the given board. This
          means there is no disk on the given board that refers to the same object. So It
          is allowed that there are copies of the given disk in the given board.
        - The function also returns True if the given disk is None.
        - This function will be used in is_playable_board. The function is_playable_board
          already checks if the given board is a proper board. (So it is assumed the given
          board is a proper board and the given disk is a proper disk.)
    """

    if disk is None:
        return False

    count = 0

    for column in range(len(board)):

        for row in range(len(board[column])):

            if disk is board[column][row]:
                count+=1

    if count == 1:
        return False

    return True


def chain_left(board, position, start_column):
    """
        Returns the length of the chain left of the disk in the given position on the given board.
    """

    if start_column < 0 or get_disk_at(board, (start_column + 1, position[1])) is None:
        return 0

    start_column -= 1

    return 1 + chain_left(board, position, start_column)


def chain_right(board, position, start_column):
    """
            Returns the length of the chain right of the disk in the given position on the given board.
    """

    if start_column == dimension(board) or get_disk_at(board, (start_column + 1, position[1])) is None:
        return 0

    start_column += 1

    return 1 + chain_right(board, position, start_column)


def print_board(board):
    """
        Print the given board.
        ASSUMPTIONS
        - The given board must be a proper board.
    """
    assert is_proper_board(board)
    # Formatting could be used to improve the layout.
    for row in range(dimension(board)+1, 0, -1):
        print(end="|")
        for col in range(1, dimension(board) + 1):
            disk = get_disk_at(board, (col, row))
            if disk == None:
                print('   ', end=" |", )
            else:
                status, value = disk
                if status == Disk.WRAPPED:
                    print('%2s' % '\u2B24', end=" |")
                elif status == Disk.CRACKED:
                    print('%4s' % '\u20DD', end=" |")
                else:  # numbered disk
                    print('%3s' % value, end=" |", )
        print()
        if row == dimension(board)+1:
            print("|"+"----|"*dimension(board))
    print()
