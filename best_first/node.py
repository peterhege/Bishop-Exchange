from check import is_white

class node:
    state = []
    parent = None
    operator = None
    applicable = []
    heuristic = 0


    def pop_operator( self, index ):
        self.applicable.pop( index )


    def get_state( self ):
        '''Print Transferred status in "chess board".'''
        chess_board = [ [ "  " ] * 4 for i in range( 5 ) ]
        chess_board_str = []

        for i in range( 8 ):
            if is_white( i ):
                chess_board[ self.state[i][0] - 1 ][ self.state[i][1] - 1 ] = "♗{id}".format( id=i )
            else:
                chess_board[ self.state[i][0] - 1 ][ self.state[i][1] - 1 ] = "♝{id}".format( id=i )

        chess_board_str.append( '\n{space}{list}'.format( space=' '*5, list='   '.join( [ ' '+str(i) for i in range( 1, 4+1 ) ] ) ) )
        chess_board_str.append( ' '*3 + '-'*21 )

        for i in range( 5 ):
            chess_board_str.append( ' {row} | {list} |'.format( row=i+1, list=' | '.join( chess_board[ i ] ) ) )
            chess_board_str.append( ' '*3 + '-'*21 )
        chess_board_str.append('')

        return '\n'.join( chess_board_str )


    def __str__( self ):
        return str( ( self.state, self.parent, self.operator, self.applicable ) )