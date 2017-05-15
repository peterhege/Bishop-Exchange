# Operator choose modes

import random
from check import is_white


def heuristic( state ):
    '''Heuristic function'''
    h = 0
    #h += heuristic_distance( state )
    #h += heuristic_distance2( state )
    h += heuristic_wrong( state )
    h += heuristic_wrong2( state )
    
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


def choose_from_keyboard( operators ):
    '''Choose operator from keyboard'''

    # Opportunities
    print( "{:^8}{:^11}".format( "Futó", "Pozíció" ) )
    print( "-" * 19 )
    for op in operators:
        print( "{:^8}{:^11}".format( op[0], str( op[1] ) ) )

    while True:
        op = input( "\nKérem, adjon meg egy operátort ( futó, pozíció 1, pozíció 1 ): ").replace(" ","").replace("(","").replace(")","").split(",")
        
        if len( op ) != 3:
            continue

        op = [ int(op[0]), ( int(op[1]), int(op[2]) ) ]

        if op in operators:
            break

        print( "Hiba: a megadott operátor nincs a listán!" )

    return op


def choose_random( operators ):
    '''Choose randomly in operators'''
    return random.choice( operators )


def choose_heuristic( operators ):
    '''Choose with heuristic'''
    operator = operators[0]
    h = operators[0][2]

    for op in operators:
        if op[2] < h:
            operator = op
            h = op[2]

    return operator


def choose_mode():
    modes = [ "Billentyűzetről", "Véletlenszerűen", "Hegymászó módszer" ]

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


def choose( operators, mode ):
    if mode == 0:
        return choose_from_keyboard( operators )
    elif mode == 1:
        return choose_random( operators )
    elif mode == 2:
        return choose_heuristic( operators )