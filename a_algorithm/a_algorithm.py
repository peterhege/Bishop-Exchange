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
                    new_node.heuristic = heuristic( state )
                    new_node.cost = nodes[selected].cost + way_costs( op, nodes[selected].state )

                    nodes.append( new_node )
                    opened.append( len( nodes ) - 1 )
                else:
                    new_cost = nodes[selected].cost + way_costs( op, nodes[selected].state )
                    if o != None:
                        if new_cost < nodes[o].cost:
                            nodes[o].parent = selected
                            nodes[o].operator = op
                            nodes[o].cost = new_cost
                    else:
                        if new_cost < nodes[c].cost:
                            nodes[c].parent = selected
                            nodes[c].operator = op
                            nodes[c].cost = new_cost
                            index = closed.index( c )
                            closed.pop( index )
                            opened.append( c )


    index = opened.index( selected )
    opened.pop( index )
    closed.append( selected )


def way_costs( op, state ):
    return abs( state[ op[0] ][0] - op[1][0] )


def a_algorithm():
    ''' Search algorithm '''

    opened = []
    closed = []
    nodes = []

    new_node = node()
    new_node.state = START
    new_node.parent = None
    new_node.operator = None
    new_node.heuristic = heuristic( START )
    new_node.cost = 0
    nodes.append( new_node )

    opened.append( 0 )

    while True:
        if len( opened ) == 0:
            break

        selected = choose_node( nodes, opened )

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
    a_algorithm()

##############################################################################

if __name__ == "__main__":
    main()
