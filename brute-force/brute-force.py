#!/usr/bin/env python3
#coding: utf-8

from check import is_white
from check import is_exist
from check import is_free
from check import is_knock
from chooses import choose
from chooses import choose_heuristics
from chooses import choose_random
from chooses import choose_from_keyboard
from chooses import choose_mode
from chooses import heuristics

# Start state
START = [
    [ 1, 1, 1, 1, 5, 5, 5, 5 ], # Row
    [ 1, 2, 3 ,4, 1, 2, 3 ,4 ]  # Column
]

# Goal state row
GOAL_ROW = [ 5, 5, 5, 5, 1, 1, 1, 1 ]

def print_state( state ):
    '''Print Transferred status in "chess board".'''
    chess_board = [ [ "[]" ] * 4 for i in range( 5 ) ]

    for i in range( 8 ):
        if i < 4:
            chess_board[ state[0][i] - 1 ][ state[1][i] - 1 ] = "{bishop}♝".format( bishop=i )
        else:
            chess_board[ state[0][i] - 1 ][ state[1][i] - 1 ] = "{bishop}♗".format( bishop=i )

    print( '\n  ', end=' ' )
    for i in range( 4 ):
        print( i + 1, end='  ')
    print( '' )

    for i in range( 5 ):
        print( i + 1, end=' ' )
        for j in range( 4 ):
            print( chess_board[i][j], end=' ' )
        print('')
    print('')


def applicable_operators( state, mode ):
    '''Return to the applicable operators'''
    operators = {}

    # way vectors
    v = [ 1, 1, -1, -1 ]
    w = [ 1, -1, 1, -1 ]

    for i in range( 8 ):                    # 8 bishop
        pos = ( state[0][i], state[1][i] )
        for k in range( 4 ):                # 4 way
            for j in range( 1, 4 ):         # 3 step (max) = 96 operators
                new_pos = ( pos[0] + v[k] * j, pos[1] + w[k] * j ) # possible position

                if not is_free( new_pos, state, i ):
                    break # If position is not free, then it cannot be crossed

                if not is_exist( new_pos ) or is_knock( new_pos, state, i ):
                    continue

                if mode == 2:
                    h = heuristics( use( state, ( i, new_pos[0], new_pos[1] ) ) )
                    if h > heuristics( state ):
                        continue

                if i not in operators:
                    operators[i] = []

                if mode == 2:
                    operators[i].append( ( new_pos[0], new_pos[1], h ) )
                else:
                    operators[i].append( new_pos )

    return operators


def use( state, operator ):
    '''Use selected operator'''
    new_state = [ state[0][:], state[1][:] ]

    new_state[0][ operator[0] ] = operator[1]
    new_state[1][ operator[0] ] = operator[2]

    return [ new_state[0][:], new_state[1][:] ]


def brute_force_search():
    ''' Search algorithm '''
    actual = START

    mode = choose_mode()

    while True:
        print_state( actual )

        if actual[0] == GOAL_ROW:
            break

        O = applicable_operators( actual, mode )
        if len( O ) != 0:
            o = choose( O, mode )
            actual = use( actual, o )
        else:
            break

    if actual[0] == GOAL_ROW:
        print( actual )
    else:
        print( "Sikertelen keresés" )


def main():
    brute_force_search()

##############################################################################

if __name__ == "__main__":
    main()
