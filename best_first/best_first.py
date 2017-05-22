#!/usr/bin/env python3
#coding: utf-8

from check import is_white
from check import is_exist
from check import is_free
from check import is_knock
from check import is_goal
from check import is_in
from chooses import choose_mode
from chooses import heuristic
from chooses import choose_node
from node import node
from collections import deque

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


def sorted_insert( opened, nodes, i, j, index ):
    if len( opened ) == 0:
        opened.append( index )
        return

    if i >= j:
        opened.insert( j, index )
        return

    half = ( i + j ) // 2

    if nodes[ opened[ half ] ].heuristic == nodes[ index ].heuristic:
        opened.insert( half, index )
        return

    if nodes[ opened[ half ] ].heuristic > nodes[ index ].heuristic:
        return sorted_insert( opened, nodes, i, half, index )
    if nodes[ opened[ half ] ].heuristic < nodes[ index ].heuristic:
        return sorted_insert( opened, nodes, half+1, j, index )


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
                    new_node.heuristic = heuristic( state )

                    nodes.append( new_node )
                    sorted_insert( opened, nodes, 0, len( opened ), len( nodes ) - 1 )

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


def best_first():
    ''' Search algorithm '''

    step = 0

    opened = deque([])
    closed = []
    nodes = []

    new_node = node()
    new_node.state = START
    new_node.parent = None
    new_node.operator = None
    new_node.heuristic = heuristic( START )
    nodes.append( new_node )

    opened.append( 0 )

    while True:
        print( "[{}{}. lépés] Keresés folyamatban...".format( (10-len(str(step)))*'-', step ), end='\r' )

        if len( opened ) == 0:
            break

        selected = opened.popleft()
        
        '''if step == 2000:
            write_nodes( opened, closed, nodes, step, selected )
            exit(0)'''
        step += 1

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
    best_first()

##############################################################################

if __name__ == "__main__":
    main()
