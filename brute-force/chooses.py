# Operator choose modes

import random
from check import is_white

def heuristics( state ):
    '''Heuristic function'''
    h = 0
    for i in range( 8 ):
        if is_white( i ):
            h += 5 - state[0][i]
        else:
            h += state[0][i] - 1

    return h


def choose_from_keyboard( operators ):
    '''Choose operator from keyboard'''

    # Opportunities
    print( "{0:<8}{1}".format( "Futó", "Választható pozíciók" ) )
    print( "-" * 40 )
    for bishop, positions in operators.items():
        print( "{0:<8}{1}".format( bishop, positions ) )

    # Select bishop
    while True:
        bishop = input( "\nKérem, adja meg a választani kívánt bábu sorszámát: " )
        if not bishop.isdigit() or int( bishop ) not in operators:
            print( "Hiba: Helytelen sorszám" )
        else:
            bishop = int( bishop )
            break

    # Select position
    while True:
        pos = input( "\nKérem, adja meg hova lépjen a kiválasztott bábu: " ).replace(" ","").split(",")

        if len( pos ) != 2 or not pos[0].isdigit() or not pos[1].isdigit():
            print( "Hiba: Helytelen pozíció" )
        else:
            row, column = int( pos[0] ), int( pos[1] )
            if ( row, column ) not in operators[ bishop ]:
                print( "Hiba: Helytelen pozíció" )
            else:
                break

    return ( bishop, row, column )


def choose_random( operators ):
    '''Choose randomly in operators'''

    # Select bishop
    while True:
        bishop = random.randint( 0, 7 )
        if bishop in operators:
            break

    # Select position
    pos = random.choice( operators[ bishop ] )

    return ( bishop, pos[0], pos[1] )


def choose_heuristics( operators ):
    '''Choose with heuristics'''
    h = 4 * 4 * 2 + 1

    for bishop, li in operators.items():
        for data in li:
            if data[2] < h:
                operator = ( bishop, data[0], data[1] )
                h = data[2]

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
        return choose_heuristics( operators )