best_solutions_so_far = [(None, None),]
    if disks == []:
        return [(0, []),]
    for column in range(len(board)):

        copy_disks = disks[:]
        score_so_far = 0
        columns_to_drop = []
        copy_board = Board.get_board_copy(board)
        k=0
        if not Board.is_full_column(copy_board, column + 1):

            score_so_far += drop_disk_at(copy_board, copy_disks[0], column + 1)
            columns_to_drop += [column + 1]
            #print(highest_score(copy_board, copy_disks[1:])[0])
            remaining_score, remaining_columns = highest_scores(copy_board, copy_disks[1:])[0]

            if remaining_score != None:

                score_so_far += remaining_score

                if remaining_columns != None:
                    columns_to_drop += remaining_columns


                if best_solutions_so_far[0][0] == None or score_so_far > best_solutions_so_far[0][0]:
                    best_solutions_so_far = [(score_so_far, columns_to_drop)]
                #score_so_far > best_solutions_so_far[0][0]:

    return best_solutions_so_far




#Board.print_board(board)

    copy_disks = disks[:]
    #copy_board = Board.get_board_copy(board)

    score_so_far = 0
    columns_to_drop = []
    best_solution_so_far = (None,None)



    if disks == []:
        return (0,[])
    for column in range(len(board)):
        #print(column)
        #print('columns_to_drop', columns_to_drop, 'score_so_far', score_so_far)
        #print('column',column)
        score_so_far = 0
        columns_to_drop = []
        copy_board = Board.get_board_copy(board)

        if not Board.is_full_column(copy_board, column+1):

            score_so_far += drop_disk_at(copy_board,copy_disks[0],column+1)
            columns_to_drop += [column+1]

            remaining_score,remaining_columns = highest_score(copy_board,copy_disks[1:])

            if remaining_score != None:

                score_so_far += remaining_score



                if remaining_columns != None:
                    columns_to_drop += remaining_columns

                print('score_so_far',score_so_far)

                if best_solution_so_far[0] == None or score_so_far > best_solution_so_far[0]:

                    #print('nieuwe high score')
                    best_solution_so_far = (score_so_far,columns_to_drop)
                    #Board.print_board(copy_board)
                    #print ('best_solution_so_far',best_solution_so_far)

    #print('columns_to_drop',columns_to_drop,'score_so_far',score_so_far)
    return best_solution_so_far



if len(disks) == 0:
    return [0, []]

for column in range(1, len(board) + 1):
    score_so_far = 0
    colums_to_drop = []

    copy_board = Board.get_board_copy(board)
    copy_disks = disks[:]

    score_so_far += drop_disk_at(copy_board, copy_disks[0], column)
    colums_to_drop += [column]

    remaining_score, remaining_colums = highest_score(copy_board, disks[1:], best_solution_so_far)

    score_so_far += remaining_score
    colums_to_drop += remaining_colums

    if score_so_far > best_solution_so_far[0]:
        best_solution_so_far = score_so_far, colums_to_drop

return (best_solution_so_far)










#     #print (columns_to_drop,highest_score_so_far)
#     copy_disks = disks[:]
#     copy_board = Board.get_board_copy(board)
#     solution  = (highest_score_so_far, columns_to_drop)
#     #print('solution', solution)
#     #print('disks',disks)
#     if len(disks) == 0:
#         #columns_to_drop = []
#         return solution
#     # return (current_score, columns_to_drop)
#         #print(best_column_last_drop,score_last_drop)
#         # if current_score > highest_score_so_far:
#         #     highest_score_so_far = current_score
#             # solution = (highest_score_so_far,columns_to_drop)
#
#
#
#
#
#     for column in range(len(board)):
#         #print ('column',column)
#         #print ('columns_to_drop hierzo', columns_to_drop)
#         disks_current_step = disks
#         board_current_step = Board.get_board_copy(board)
#         current_score_current_step = current_score
#         #print ('current_score_current_step',current_score_current_step)
#         columns_to_drop_current_step = columns_to_drop[:]
#         #print('disks_current_step',disks_current_step)
#         columns_to_drop.append(column+1)
#         current_score += drop_disk_at(copy_board,copy_disks[0],column+1)
#         #print ('copy_board',copy_board)
#         #Board.print_board(copy_board)
#         #print ('solution',solution)
#         #print (highest_score(copy_board,disks[1:],current_score,highest_score_so_far,columns_to_drop))
#         solution = highest_score(copy_board,disks[1:],current_score,highest_score_so_far,columns_to_drop)
#         print ('solution',solution)
#         highest_score_so_far = solution[1]
#         #highest_score_so_far,columns_to_drop = highest_score(copy_board,disks[1:],current_score,highest_score_so_far,columns_to_drop)
#         #print ('solution  na ', solution)
#         #print('current_score',current_score)
#         #print('highest_score_so_far',highest_score_so_far)
#         #print ('(highest_score_so_far, columns_to_drop)',(highest_score_so_far, columns_to_drop))
#         #print ('current_score',current_score)
#         print (highest_score_so_far,'columns_to_drop',columns_to_drop)
#         #print ('current_score',current_score,'highest_score_so_far',highest_score_so_far)
#         if current_score > highest_score_so_far:
#             print ('nieuwe high scoreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
#             highest_score_so_far = current_score
#             #print('zekers')
#             solution = (highest_score_so_far, columns_to_drop)
#             #print ('solution',solution)
#             #print('solution',solution)
#         #print ('zekers')
#         #highest_score_so_far = current_highest_score
#         current_score = current_score_current_step
#         #print ('current_score',current_score)
#         print (('columns_to_drop niet verwijderd', columns_to_drop))
#         #columns_to_drop = columns_to_drop[:-1]
#         #print('columns_to_drop verwijderd', columns_to_drop)
#         #columns_to_drop[:-1]
#         disks = disks_current_step
#         copy_board = board_current_step
#         columns_to_drop = columns_to_drop_current_step
#         #print('disks',disks)
#         #print('board     ',board)
#        # print('copy_board',copy_board)
#         #Board.print_board(board)
#         print ('column',column)
#         #print('columns_to_drop verwijderd',columns_to_drop)
#         print('columns_to_drop verwijderd', columns_to_drop)
#
#     print('to_be_returned',solution)
#     # current_score = 0
#     # #highest_score_so_far = 0
#     # columns_to_drop = []
#     return solution
#     #     if current_score >= highest_score_so_far:
#     #         highest_score_so_far = current_score
#     #         best_solution_so_far = (highest_score_so_far, columns_to_drop)
#     #         print(best_solution_so_far,'best_solution_so_far')
#     #         return best_solution_so_far
#     # highest_score(board,disks[1:],current_score,highest_score_so_far,columns_to_drop)
#     # print (best_solution_so_far)
#
# #print (best_drop_for_disk([[[20, 2], None, None, None, None], [[30, 1], [30, 4], None, None, None], [[30, 3], [20, 4], [30, 2], [10, 2], None], [[20, 1], None, None, None, None]],[10, 2]))
#
# #print(drop_disk_at([[[20, 2], None, None, None, None], [[30, 1], [30, 4], None, None, None], [[30, 3], [20, 4], [30, 2], [10, 2], None], [[20, 1], None, None, None, None]],[10, 2],0))
#
# #print([[[20, 2], None, None, None, None], [[30, 1], [30, 4], None, None, None], [[30, 3], [20, 4], [30, 2], [10, 2], None], [[20, 1], None, None, None, None]])
#
# #Board.print_board([[[20, 2], None, None, None, None], [[30, 1], [30, 4], None, None, None], [[30, 3], [20, 4], [30, 2], [10, 2], None], [[20, 1], None, None, None, None]])
#
#     # best_solution_so_far = None
#     # if len(disks) == 0:
#     #     return
#     # print(current_score,highest_score_so_far,columns_to_drop)
#     # print ('disks',disks)
#     # if len(disks) == 1:
#     #     print ('copy_board',copy_board)
#     #     print ('copy_disks',copy_disks)
#     #     #print('best_drop_for_disk',best_drop_for_disk(copy_board,copy_disks))
#     #     best_column_last_drop,score_last_drop = best_drop_for_disk(copy_board,copy_disks)
#     #     current_score += score_last_drop
#     #     columns_to_drop.append(best_column_last_drop)
#     #     print ('zekers')
#     #     print('current_score',current_score)
#     #     if current_score >= highest_score_so_far:
#     #         highest_score_so_far = current_score
#     #         best_solution_so_far = (highest_score_so_far, columns_to_drop)
#     #         print(best_solution_so_far,'best_solution_so_far')
#     #         return best_solution_so_far
#     # highest_score(board,disks[1:],current_score,highest_score_so_far,columns_to_drop)
#     # print (best_solution_so_far)
#
# #print(testbord,test_disks)
#
# #highest_score(test_board,test_disk)
#
#
# # if len(disks) == 1:
# #     last_disk = copy_disks[0]
# #     best_column_last_drop,score_last_drop = best_drop_for_disk(copy_board,last_disk)
# #     #print(best_column_last_drop,score_last_drop)
# #     if best_column_last_drop == len(board) and \
# #             drop_disk_at(Board.get_board_copy(board),Disk.get_disk_copy(disks[0]),1)== \
# #             drop_disk_at(Board.get_board_copy(board), Disk.get_disk_copy(disks[0]),len(board)):
# #         print('switch')
# #         best_column_last_drop = 1
# #     current_score += score_last_drop
# #     columns_to_drop.append(best_column_last_drop)
# #     print ('last_return',(current_score, columns_to_drop))
# #     return (current_score, columns_to_drop)
# copy_disks = disks[:]
#     copy_board = Board.get_board_copy(board)
#     solution = (highest_score_so_far, columns_to_drop)
#
#     if len(disks) == 0:
#         return solution
#
#     for column in range(len(board)):
#         disks_current_step = disks
#         board_current_step = Board.get_board_copy(board)
#         current_score_current_step = current_score
#
#         columns_current_step = current_columns[:]
#
#         current_columns.append(column+1)
#         current_score += drop_disk_at(copy_board,copy_disks[0],column+1)
#         solution = highest_score(copy_board,disks[1:],current_score,highest_score_so_far,current_columns)
#         print ('solution',solution)
#         highest_score_so_far = solution[0]
#         print (highest_score_so_far,'current_columns',current_columns)
#         if current_score > highest_score_so_far:
#             print ('nieuwe high scoreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
#             highest_score_so_far = current_score
#             solution = (highest_score_so_far, current_columns)
#             print ('solution hier',solution)
#             columns_to_drop = current_columns[:]
#         current_score = current_score_current_step
#         print (('current_columns niet verwijderd', current_columns))
#
#         disks = disks_current_step
#         copy_board = board_current_step
#         current_columns = columns_current_step
#
#         print ('column',column)
#         print('current_columns verwijderd', current_columns)
#
#     print('to_be_returned',solution)
#
#     return solution