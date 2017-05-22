# Operator choose modes

import random
from check import is_white


def heuristic( state ):
    '''Heuristic function'''
    h = 0
    h += heuristic_distance( state )
    #h += heuristic_distance2( state )
    #h += heuristic_wrong( state )
    #h += heuristic_wrong2( state )
    
    return h


def heuristic_wrong( state ):
    h = 0
    for i in range( 8 ):
        if is_white( i ):
            if state[i][0] == 1:
                h += 2
            if state[i][0] != 5:
                h += 1
        else:
            if state[i][0] == 5:
                h += 2
            if state[i][0] != 1:
                h += 1

    return h


def heuristic_wrong2( state ):
    h = 0
    for i in range( 8 ):
        if ( i * state[i][1] ) % 2 == 0:
            h += 1
        elif ( i * state[i][1] ) % 2 == 1:
            h += 1

    return h


def heuristic_distance( state ):
    h = 0
    for i in range( 8 ):
        if is_white( i ):
            h += 5 - state[i][0]
        else:
            h += state[i][0] - 1

    return h


def heuristic_distance2( state ):
    h = 0
    whites_is_wrong = False

    for i in range( 4 ):
        if state[i] != 5:
            whites_is_wrong = True
            break

    if whites_is_wrong:
        for i in range( 4 ):
            h += 5 - state[i][0]
    else:
        for i in range( 4, 8 ):
            h += state[i][0] - 1

    return h


def choose_heuristic( operators ):
    '''Choose with heuristic'''
    return choose_first( operators )


def choose_mode():
    modes = [ "Szélességi", "Mélységi" ]

    print( "{id:^13}{mode}".format( id="Azonosító", mode="Választás módja" ) )
    print( "-" * 40 )
    for i in range( len( modes ) ):
        print( "{id:^13}{mode}".format( id=i, mode=modes[i] ) )

    while True:
        mode = input("\nKérem adja meg a választás módjának azonosítóját: ")

        if not( mode.isdigit() and int( mode ) in range( len( modes ) ) ):
            print( "Hiba: helytelen azonosító" )
        else:
            return int( mode )


def choose_node( nodes, opened ):
    index = opened[0]

    for i in opened:
        if nodes[i].cost < nodes[index].cost:
            index = i

    return index