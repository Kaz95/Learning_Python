# TODO RPG Inventory Project at end of chapter 6

# Basic tic tac toe program for two players
# Example for formatting real world data via data structures.

# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
#
#
# def print_board(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#
#
# turn = 'X'
# for i in range(9):
#     print_board(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'
#
# print_board(theBoard)


# Inventory checker.
# Good .get() method example


# all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
#               'Bob': {'ham sandwiches': 3, 'apples': 2},
#               'Carol': {'cups': 3, 'apple pies': 1}}
#
#
# def total_brought(guests, item):
#     num_bought = 0
#     for k, v in guests.items():
#         num_bought = num_bought + v.get(item, 0)
#     return num_bought
#
#
# print('Number of things being brought:')
# print(' - Apples        ' + str(total_brought(all_guests, 'apples')))
# print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
# print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
# print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
# print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))
