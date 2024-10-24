ALL_SPACES = list('123456789') 
X, O, BLANK = 'X', 'O', ' ' 

class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        """Create a new, blank tic tac toe board."""
        self._spaces = {}  # The board is represented as a Python dictionary.
        for space in ALL_SPACES:
            self._spaces[space] = BLANK  # All spaces start as blank.

    def getBoardStr(self):
        """Return a text-representation of the board."""
        return f'''
      {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']}  1 2 3
      -+-+-
      {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']}  4 5 6
      -+-+-
      {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']}  7 8 9'''
    
    """
    print(board.getBoardStr())

    Result
        | |   1 2 3
        -+-+-
        | |   4 5 6
        -+-+-
        | |   7 8 9
    """

    def isValidSpace(self, space):
        """Returns True if the space on the board is a valid space number
        and the space is blank."""
        return space in ALL_SPACES and self._spaces[space] == BLANK
    
    """
    print(board.isValidSpace('2'))

    Result = True
    """

board = TTTBoard()

print(board.getBoardStr())

print(board.isValidSpace('2'))