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


def get_solution( nodes, index, li ):
    solution = []

    while index != None:
        data = []
        if 'op' in li:
            data.append( 'operator: {op}'.format( op=nodes[ index ].operator ) )
        if 'co' in li:
            data.append( 'cost={co}'.format( co=nodes[ index ].cost ) )

        solution.append( '{data}:\n{state}\n'.format( data=', '.join( data ), state=nodes[ index ].get_state() ) )
        index = nodes[ index ].parent

    return solution[::-1]


def search( li, state, nodes ):
    for i in li:
        if state == nodes[i].state:
            return i

    return None

def way_costs( op, state ):
    step = abs( state[ op[0] ][0] - op[1][0] )
    if is_white( op[0] ) and op[1][0] < state[ op[0] ][0]:
        step *= 2
    elif not is_white( op[0] ) and op[1][0] > state[ op[0] ][0]:
        step *= 2

    return step


def sorted_insert( opened, nodes, i, j, index ):
    if len( opened ) == 0:
        opened.append( index )
        return

    if i >= j:
        opened.insert( j, index )
        return

    half = ( i + j ) // 2

    if nodes[ opened[ half ] ].cost == nodes[ index ].cost:
        opened.insert( half, index )
        return

    if nodes[ opened[ half ] ].cost > nodes[ index ].cost:
        return sorted_insert( opened, nodes, i, half, index )
    if nodes[ opened[ half ] ].cost < nodes[ index ].cost:
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
                    new_node.cost = nodes[selected].cost + way_costs( op, nodes[selected].state )

                    nodes.append( new_node )
                    sorted_insert( opened, nodes, 0, len( opened ), len( nodes ) - 1 )
                elif o != None:
                    new_cost = nodes[selected].cost + way_costs( op, nodes[selected].state )
                    if new_cost < nodes[o].cost:
                        nodes[o].parent = selected
                        nodes[o].operator = op
                        nodes[o].cost = new_cost

                        index = opened.index( o )
                        opened.pop( index )
                        sorted_insert( opened, nodes, 0, len( opened ), o )

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


def optimal_search():
    ''' Search algorithm '''

    step = 0

    opened = []
    closed = []
    nodes = []

    new_node = node()
    new_node.state = START
    new_node.parent = None
    new_node.operator = None
    new_node.cost = 0
    nodes.append( new_node )

    opened.append( 0 )

    while True:
        print( "[{}{}. lépés] Keresés folyamatban...".format( (10-len(str(step)))*'-', step ), end='\r' )

        if len( opened ) == 0:
            break

        selected = opened.pop(0)
        
        '''if step == 1500:
            write_nodes( opened, closed, nodes, step, selected )
            exit(0)'''
        step += 1

        if is_goal( nodes[ selected ].state, GOAL_ROWS ):
            break

        extend( selected, opened, closed, nodes  )

    if len( opened ) != 0:
        solution = get_solution( nodes, selected, [ 'op', 'he', 'co' ] )

        with open( 'solution.txt', 'w' ) as f:
            for i in range( len(solution) ):
                f.write( '{i:2d}. {node}'.format( i=i, node=solution[i] ) )

        print( "Megoldás: solution.txt" )
    else:
        print( "Nincs megoldás" )


def main():
    optimal_search()

##############################################################################

if __name__ == "__main__":
    main()
