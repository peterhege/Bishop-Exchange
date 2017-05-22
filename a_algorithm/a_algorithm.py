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


def get_solution( nodes, index, li ):
    solution = []

    while index != None:
        data = []
        if 'op' in li:
            data.append( 'operator: {op}'.format( op=nodes[ index ].operator ) )
        if 'he' in li:
            data.append( 'h(state)={he}'.format( he=nodes[ index ].heuristic ) )
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
                    new_node.heuristic = heuristic( state )

                    opened.append( len( nodes ) )
                    nodes.append( new_node )
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
    step = abs( state[ op[0] ][0] - op[1][0] )
    if is_white( op[0] ) and op[1][0] < state[ op[0] ][0]:
        step *= 2
    elif not is_white( op[0] ) and op[1][0] > state[ op[0] ][0]:
        step *= 2

    return step


def write_nodes( opened, closed, nodes, step, selected ):
    one_step = []
    one_step.append( "{step}. lépés\n".format( step=step ) )
    one_step.append( "\nNyíltak:\n" )
    if opened:
        for i in opened:
            predicted_cost = 0
            real_cost = 0
            if nodes[i].parent:
                predicted_cost = nodes[ nodes[i].parent ].heuristic - nodes[i].heuristic
                real_cost = nodes[i].cost - nodes[ nodes[i].parent ].cost
            s = ''
            if i == selected:
                s = '->'
            elif is_goal( nodes[ selected ].state, GOAL_ROWS ):
                s = 'cél->'
            one_step.append( '{s}{node} {a}\n'.format( s=s, node=str( nodes[i] ), a=predicted_cost<=real_cost ) )

    one_step.append( "\nZártak:\n" )
    if closed:
        for i in closed:
            predicted_cost = 0
            if nodes[i].parent:
                predicted_cost = nodes[ nodes[i].parent ].heuristic - nodes[i].heuristic
                real_cost = nodes[i].cost - nodes[ nodes[i].parent ].cost
            one_step.append( '{node} {a}\n'.format( node=str( nodes[i] ), a=predicted_cost<=real_cost ) )


    with open( "test/test{}.txt".format(step), "w" ) as f:
        f.write( ''.join( one_step ) )


def a_algorithm():
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
    new_node.heuristic = heuristic( START )
    nodes.append( new_node )

    opened.append( 0 )

    while True:
        print( "[{}{}. lépés] Keresés folyamatban...".format( (10-len(str(step)))*'-', step ), end='\r' )

        if len( opened ) == 0:
            break

        selected = choose_node( nodes, opened )
        '''if step%500==0:
            write_nodes( opened, closed, nodes, step, selected )
        if step==100000:
            exit(0)'''
        step += 1

        #print( nodes[ selected ].get_state() )

        if is_goal( nodes[ selected ].state, GOAL_ROWS ):
            break

        extend( selected, opened, closed, nodes  )

    print('')

    if len( opened ) != 0:
        solution = get_solution( nodes, selected, [ 'op', 'he', 'co' ] )

        with open( 'solution.txt', 'w' ) as f:
            for i in range( len(solution) ):
                f.write( '{i:2d}. {node}'.format( i=i, node=solution[i] ) )

        print( "Megoldás: solution.txt" )
    else:
        solution = get_solution( nodes, selected, [ 'op', 'he', 'co' ] )

        with open( 'solution.txt', 'w' ) as f:
            for i in range( len(solution) ):
                f.write( '{i:2d}. {node}'.format( i=i, node=solution[i] ) )
        print( "Nincs megoldás" )


def main():
    a_algorithm()

##############################################################################

if __name__ == "__main__":
    main()
