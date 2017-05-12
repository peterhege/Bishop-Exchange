#!/usr/bin/env python3
#coding: utf-8

import random

# Start state
START = [
    [ 1, 1, 1, 1, 5, 5, 5, 5 ], # Row
    [ 1, 2, 3 ,4, 1, 2, 3 ,4 ]  # Column
]

# Goal state row
GOAL_ROW = [ 5, 5, 5, 5, 1, 1, 1, 1 ]

def print_state( state ):
    '''Print Transferred status in "chess board".'''
    chess_board = [ [ "[]" ] * 4 for i in range( 5 ) ]

    for i in range( 8 ):
        if i < 4:
            chess_board[ state[0][i] - 1 ][ state[1][i] - 1 ] = "{bishop}♝".format( bishop=i )
        else:
            chess_board[ state[0][i] - 1 ][ state[1][i] - 1 ] = "{bishop}♗".format( bishop=i )

    print( '\n  ', end=' ' )
    for i in range( 4 ):
        print( i + 1, end='  ')
    print( '' )

    for i in range( 5 ):
        print( i + 1, end=' ' )
        for j in range( 4 ):
            print( chess_board[i][j], end=' ' )
        print('')
    print('')


def is_white( bishop ):
    if bishop < 4:
        return True
    return False


def is_exist( pos ):
    '''Is the position exist on the chessboard?'''
    return pos[0] >= 1 and pos[0] <= 5 and pos[1] >= 1 and pos[1] <= 4


def is_free( pos, state, bishop ):
    '''Is the position free on the chessboard?'''
    for i in range( 8 ):
        if i != bishop:
            if pos == ( state[0][i], state[1][i] ):
                return False
    return True


def is_knock( pos, state, bishop ):
    '''Knock a bishop here?'''
    if is_white( bishop ):
        r = range( 4, 8 )
    else:
        r = range( 4 )

    for i in r:
        if abs( state[0][i] - pos[0] ) == abs( state[1][i] - pos[1] ):
            return True

    return False


def applicable_operators( state ):
    '''Return to the applicable operators'''
    operators = {}

    # way vectors
    v = [ 1, 1, -1, -1 ]
    w = [ 1, -1, 1, -1 ]

    for i in range( 8 ):                    # 8 bishop
        pos = ( state[0][i], state[1][i] )
        for k in range( 4 ):                # 4 way
            for j in range( 1, 4 ):         # 3 step (max) = 96 operators
                new_pos = ( pos[0] + v[k] * j, pos[1] + w[k] * j ) # possible position

                if not is_exist( new_pos ):
                    continue

                if not is_free( new_pos, state, i ):
                    break # If position is not free, then it cannot be crossed

                if is_knock( new_pos, state, i ):
                    continue

                if i not in operators:
                    operators[i] = []
                operators[i].append( new_pos )

    return operators


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
    pass


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


def use( state, operator ):
    '''Use selected operator'''
    state[0][ operator[0] ] = operator[1]
    state[1][ operator[0] ] = operator[2]

    return state


def brute_force_search():
    ''' Search algorithm '''
    actual = START

    mode = choose_mode()

    while True:
        print_state( actual )

        if actual[0] == GOAL_ROW:
            break

        O = applicable_operators( actual )
        if len( O ) != 0:
            o = choose( O, mode )
            actual = use( actual, o )
        else:
            break

    if actual[0] == GOAL_ROW:
        print( actual )
    else:
        print( "Sikertelen keresés" )


def main():
    brute_force_search()

##############################################################################

if __name__ == "__main__":
    main()
