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