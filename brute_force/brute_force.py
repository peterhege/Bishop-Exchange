#!/usr/bin/env python3
#coding: utf-8

from check import is_white
from check import is_exist
from check import is_free
from check import is_knock
from check import is_goal
from chooses import choose
from chooses import choose_heuristic
from chooses import choose_random
from chooses import choose_from_keyboard
from chooses import choose_mode
from chooses import heuristic

# Start state
START = [
    (1,1), (1,2), (1,3), (1,4), # White
    (5,1), (5,2), (5,3), (5,4)  # Black
]

# Goal state row
GOAL_ROWS = [
    5, 5, 5, 5, # White
    1, 1, 1, 1  # Black
]

def print_state( state ):
    '''Print Transferred status in "chess board".'''
    chess_board = [ [ "  " ] * 4 for i in range( 5 ) ]

    for i in range( 8 ):
        if is_white( i ):
            chess_board[ state[i][0] - 1 ][ state[i][1] - 1 ] = "♗{id}".format( id=i )
        else:
            chess_board[ state[i][0] - 1 ][ state[i][1] - 1 ] = "♝{id}".format( id=i )

    print( '\n{space}{list}'.format( space=' '*5, list='   '.join( [ ' '+str(i) for i in range( 1, 4+1 ) ] ) ) )
    print( ' '*3 + '-'*21 )

    for i in range( 5 ):
        print( ' {row} | {list} |'.format( row=i+1, list=' | '.join( chess_board[ i ] ) ) )
        print( ' '*3 + '-'*21 )
    print('')


def applicable_operators( state, is_h=False ):
    '''Return to the applicable operators'''
    operators = []

    # way vectors
    v = [ 1, 1, -1, -1 ]
    w = [ 1, -1, 1, -1 ]

    for i in range( 8 ):            # 8 bishop
        pos = state[i]
        for k in range( 4 ):        # * 4 way
            for j in range( 1, 4 ): # * (max) 3 step = 96 operators
                new_pos = ( pos[0] + v[k] * j, pos[1] + w[k] * j ) # possible position

                if not is_free( new_pos, state, i ):
                    break # If position is not free, then it cannot be crossed

                if not is_exist( new_pos ) or is_knock( new_pos, state, i ):
                    continue

                if is_h:
                    h = heuristic( use( state, [ i, new_pos ] ) )
                    if h > heuristic( state ):
                        continue

                if is_h:
                    op = [ i, new_pos, h ]
                else:
                    op = [ i, new_pos ]

                operators.append( op )

    return operators


def use( state, operator ):
    '''Use selected operator'''
    new_state = state[:]

    new_state[ operator[0] ] = operator[1]

    return new_state


def brute_force_search():
    ''' Search algorithm '''
    actual = START

    print_state( actual )

    mode = choose_mode()

    while True:
        print_state( actual )

        if is_goal( actual, GOAL_ROWS ):
            break

        if mode == 2:
            O = applicable_operators( actual, True )
        else:
            O = applicable_operators( actual )

        if len( O ) != 0:
            o = choose( O, mode )
            actual = use( actual, o )
        else:
            break

    if is_goal( actual, GOAL_ROWS ):
        print( actual )
    else:
        print( "Sikertelen keresés" )


def main():
    brute_force_search()

##############################################################################

if __name__ == "__main__":
    main()
