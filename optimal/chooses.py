# Operator choose modes

import random
from check import is_white


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