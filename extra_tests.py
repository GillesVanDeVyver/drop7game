import Position
import Board
import Disk
import Drop7
# This file contains some tests for all helper functions used in the practicum.

# Tests position:
# is_natural_number
assert not Position.is_natural_number([1])
assert not Position.is_natural_number((1,))
assert Position.is_natural_number(78)
assert not Position.is_natural_number(-3)
assert not Position.is_natural_number(0)
assert not Position.is_natural_number(1.3)
assert not Position.is_natural_number(-1.3)

# Tests board:
# First the setup from Board_Test is copied in order to use the test boards.

wrapped_disk_value_1 = None
wrapped_disk_value_2 = None
wrapped_disk_value_3 = None
wrapped_disk_value_3_B = None
wrapped_disk_value_3_C = None
wrapped_disk_value_5 = None
visible_disk_value_1 = None
visible_disk_value_2 = None
visible_disk_value_2_B = None
visible_disk_value_3 = None
visible_disk_value_3_B = None
visible_disk_value_4 = None
visible_disk_value_6 = None
cracked_disk_value_1 = None
cracked_disk_value_1_B = None
cracked_disk_value_3 = None
cracked_disk_value_4 = None
test_board_4 = None
test_board_6 = None

def set_up():
    """
       This function initializes a large number of disks and two boards
       that can be used in tests. Such a test will then start with an
       invocation of this function
    """
    global\
        wrapped_disk_value_1, wrapped_disk_value_2, wrapped_disk_value_3, \
                wrapped_disk_value_3_C, wrapped_disk_value_3_B, wrapped_disk_value_5, \
        visible_disk_value_1, visible_disk_value_2, visible_disk_value_2_B, \
                visible_disk_value_3, visible_disk_value_3_B, visible_disk_value_4, \
                visible_disk_value_6, \
        cracked_disk_value_1, cracked_disk_value_1_B, cracked_disk_value_3, \
                cracked_disk_value_4, \
        test_board_4, test_board_6

    wrapped_disk_value_1 = Disk.init_disk(Disk.WRAPPED, 1)
    wrapped_disk_value_2 = Disk.init_disk(Disk.WRAPPED, 2)
    wrapped_disk_value_3 = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_B = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_3_C = Disk.init_disk(Disk.WRAPPED, 3)
    wrapped_disk_value_5 = Disk.init_disk(Disk.WRAPPED, 5)

    visible_disk_value_1 = Disk.init_disk(Disk.VISIBLE, 1)
    visible_disk_value_2 = Disk.init_disk(Disk.VISIBLE, 2)
    visible_disk_value_2_B = Disk.init_disk(Disk.VISIBLE, 2)
    visible_disk_value_3 = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_3_B = Disk.init_disk(Disk.VISIBLE, 3)
    visible_disk_value_4 = Disk.init_disk(Disk.VISIBLE, 4)
    visible_disk_value_6 = Disk.init_disk(Disk.VISIBLE, 6)

    cracked_disk_value_1 = Disk.init_disk(Disk.CRACKED, 1)
    cracked_disk_value_1_B = Disk.init_disk(Disk.CRACKED, 1)
    cracked_disk_value_3 = Disk.init_disk(Disk.CRACKED, 3)
    cracked_disk_value_4 = Disk.init_disk(Disk.CRACKED, 4)

    test_board_4 = Board.init_board \
        (dimension=4, given_disks= \
            ((wrapped_disk_value_3,),
             [],
             (visible_disk_value_1, cracked_disk_value_1, wrapped_disk_value_2, visible_disk_value_3)))

    test_board_6 = Board.init_board \
        (dimension=6, given_disks= \
            ((wrapped_disk_value_3,),
             [wrapped_disk_value_3_B, wrapped_disk_value_5],
             (visible_disk_value_6, visible_disk_value_3_B, wrapped_disk_value_1),
             (visible_disk_value_1, cracked_disk_value_1,
                    visible_disk_value_4, visible_disk_value_3),
             (cracked_disk_value_1_B,),
             [wrapped_disk_value_3_C, visible_disk_value_2_B]))

set_up()
# disk_on_several_positions:
assert not Board.disk_on_several_positions(visible_disk_value_1,test_board_4)
extra_test_board1 = Board.init_board(3,[[[30, 3], None, None, None],
                                        [[30, 3],[30, 5], None, None,],
                                        [[10, 6], [10, 3], [30, 1], None]])

assert Board.disk_on_several_positions([30, 3],extra_test_board1)
assert not Board.disk_on_several_positions(None,extra_test_board1)

# chain_left
assert Board.chain_left(test_board_4,(3,1),1) == 0
assert Board.chain_left(test_board_6,(3,1),1) == 2
assert Board.chain_right(test_board_6,(4,2),2) == 2

# chain right
assert Board.chain_left(test_board_4,(3,1),3) == 0
assert Board.chain_right(test_board_6,(3,1),3) == 3
assert Board.chain_right(test_board_6,(4,2),3) == 1

# Tests Drop7:
Drop7.do_explosions(test_board_6)
assert test_board_6 == [[[30, 3], None, None, None, None, None, None], [[10, 3], [20, 5], None, None, None, None, None], [None, None, None, None, None, None, None], [None, None, None, None, None, None, None], [None, None, None, None, None, None, None], [[10, 3], None, None, None, None, None, None]]

Drop7.do_explosions(test_board_4)
assert test_board_4 ==[[[30, 3], None, None, None, None], [None, None, None, None, None], [[20, 2], [10, 3], None, None, None], [None, None, None, None, None]]

extra_test_board2 = Board.init_board(5,((wrapped_disk_value_3,),
                                        (wrapped_disk_value_2,wrapped_disk_value_5,),
                                        (visible_disk_value_4, visible_disk_value_4, wrapped_disk_value_2,)))
test_board_old = Board.get_board_copy(extra_test_board2)
Drop7.do_explosions(extra_test_board2)
assert test_board_old == extra_test_board2