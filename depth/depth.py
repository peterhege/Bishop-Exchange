#!/usr/bin/env python3
#coding: utf-8

from check import is_white
from check import is_exist
from check import is_free
from check import is_knock
from check import is_goal
from check import is_in
from chooses import choose_mode
from chooses import choose_node
from collections import deque
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


def search( li, state, nodes ):
    for i in li:
        if state == nodes[i].state:
            return i

    return None


def extend( selected, opened, closed, nodes ):
    # way vectors
    v = [ 1, 1, -1, -1 ]
    w = [ 1, -1, 1, -1 ]

    for i in range( 8 ):            # 8 bishop
        pos = nodes[selected].state[i]
        for k in range( 4 ):        # * 4 way
            for j in range( 1, 4 ): # * (max) 3 step = 96 operators
                new_pos = ( pos[0] + v[k] * j, pos[1] + w[k] * j ) # possible position

                if not is_free( new_pos, nodes[selected].state, i ):
                    break # If position is not free, then it cannot be crossed

                if not is_exist( new_pos ) or is_knock( new_pos, nodes[selected].state, i ):
                    continue

                op = [ i, new_pos ]

                state = use( nodes[selected].state, op )
                o = search( opened, state, nodes )
                c = search( closed, state, nodes )

                if o == None and c == None:
                    new_node = node()
                    new_node.state = state
                    new_node.parent = selected
                    new_node.operator = op
                    new_node.depth = nodes[selected].depth + 1

                    nodes.append( new_node )
                    opened.append( len( nodes ) - 1 )

    #index = opened.index( selected )
    #opened.pop( index )
    closed.append( selected )


def write_nodes( opened, closed, nodes, step, selected ):
    one_step = []
    one_step.append( "{step}. lépés\n".format( step=step ) )
    one_step.append( "\nKiválasztott:\n" )
    one_step.append( '{node}\n'.format( node=str( nodes[selected] ) ) )
    one_step.append( "\nNyíltak:\n" )
    if opened:
        for i in opened:
            s = ''
            if is_goal( nodes[ selected ].state, GOAL_ROWS ):
                s = 'cél->'
            one_step.append( '{s}{node}\n'.format( s=s, node=str( nodes[i] ) ) )

    one_step.append( "\nZártak:\n" )
    if closed:
        for i in closed:
            one_step.append( '{node}\n'.format( node=str( nodes[i] ) ) )


    with open( "test/test{}.txt".format(step), "w" ) as f:
        f.write( ''.join( one_step ) )


def depth():
    ''' Search algorithm '''
    step = 0

    if( len( sys.argv ) == 1 ):
        mode = choose_mode()
    else:
        mode = int( sys.argv[1] )

    if mode == 0:
        opened = deque([])
    elif mode == 1:
        opened = []

    closed = []
    nodes = []

    new_node = node()
    new_node.state = START
    new_node.parent = None
    new_node.operator = None
    new_node.depth = 0
    nodes.append( new_node )

    opened.append( 0 )

    while True:
        if len( opened ) == 0:
            break

        if mode == 0:
            selected = opened.popleft()
        elif mode == 1:
            selected = opened.pop()

        '''if step == 500:
            write_nodes( opened, closed, nodes, step, selected )
            exit(0)
        step += 1'''

        print( nodes[ selected ].get_state() )

        if is_goal( nodes[ selected ].state, GOAL_ROWS ):
            break

        extend( selected, opened, closed, nodes  )

    if len( opened ) != 0:
        states = get_solution_states( nodes, selected )
        operators = get_solution_operators( nodes, selected )

        f = open( 'solution.txt', 'w' )
        for i in range( len(states) ):
            f.write( '{i:2d}. {op}:\n{state}\n'.format( i=i, op=operators[i], state=states[i] ) )

        f.close()

        print( "Megoldás: solution.txt" )
    else:
        print( "Nincs megoldás" )


def main():
    depth()

##############################################################################

if __name__ == "__main__":
    main()
