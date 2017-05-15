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
from chooses import choose_mode
from chooses import heuristic
from node import node

import sys

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


def get_solution_operators( nodes, index ):
    operators = []

    while index != None:
        operators.append( str(nodes[ index ].operator) )
        index = nodes[ index ].parent

    return operators[::-1]


def get_solution_states( nodes, index ):
    states = []

    while index != None:
        states.append( nodes[ index ].get_state() )
        index = nodes[ index ].parent

    return states[::-1]


def backtrack_search():
    ''' Search algorithm '''
    progress = 0
    li = ['|','/','-','\\']

    nodes = []

    new_node = node()
    new_node.state = START
    new_node.parent = None
    new_node.operator = None
    new_node.applicable = applicable_operators( new_node.state )
    nodes.append( new_node )
    actual = len( nodes ) - 1

    while True:
        print( li[progress], end='\r' )

        if actual == None:
            break

        if is_goal( nodes[ actual ].state, GOAL_ROWS ):
            break

        if len( nodes[ actual ].applicable ) != 0:
            index = choose( nodes[ actual ].applicable )
            operator = nodes[ actual ].applicable[ index ]
            nodes[ actual ].pop_operator( index )

            new_node = node()
            new_node.state = use( nodes[ actual ].state, operator )
            new_node.parent = actual
            new_node.operator = operator
            new_node.applicable = applicable_operators( new_node.state )
            nodes.append( new_node )
            actual = len( nodes ) - 1
        else:
            actual = nodes[ actual ].parent

        progress = ( progress + 1 ) % 4

    if actual != None:
        states = get_solution_states( nodes, actual )
        operators = get_solution_operators( nodes, actual )

        f = open( 'solution.txt', 'w' )
        for i in range( len(states) ):
            f.write( '{i:2d}. {op}:\n{state}\n'.format( i=i, op=operators[i], state=states[i] ) )

        f.close()
    else:
        print( "Nincs megoldás" )


def main():
    backtrack_search()

##############################################################################

if __name__ == "__main__":
    main()