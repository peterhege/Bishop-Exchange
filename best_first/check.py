# Checks

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
        if i == bishop:
            continue
        if pos == state[i]:
            return False
    return True


def is_knock( pos, state, bishop ):
    '''Knock a bishop here?'''
    if is_white( bishop ):
        r = range( 4, 8 )
    else:
        r = range( 4 )

    for i in r:
        if abs( state[i][0] - pos[0] ) == abs( state[i][1] - pos[1] ):
            return True

    return False


def is_goal( state, rows ):
    '''Is the state goal?'''
    for i in range( 8 ):
        if state[i][0] != rows[i]:
            return False
    return True


def is_in( nodes, actual ):
    for i in range( len( nodes ) ):
        if actual != i and nodes[ actual ].state == nodes[ i ].state:
            return True

    return False