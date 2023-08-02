#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: Rashfiqur Rahman
# email:rash@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Wasay Rizwan
# partner's email: wasayr1@bu.edu
#

from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
        
    #Function 1
    def __init__(self, init_board, init_predecessor, init_move):
        """constructor for the State class"""
        self.board = init_board
        self.predecessor = init_predecessor
        self.move = init_move
        self.num_moves =0
        if self.predecessor == None:
            self.num_moves = 0
        else:
            self.num_moves = init_predecessor.num_moves + 1
      
                
    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def is_goal(self):
        """returns True if called State object is a goal state, 
        False otherwise"""
        if GOAL_TILES == self.board.tiles:
            return True
        else:
            return False
    def generate_successors(self):
        """creates and returns a list of State objects for all
        successor states of the called State object"""
        successors = []
        for m in MOVES:
            b = self.board.copy()
            if b.move_blank(m) == True:
                new_obj = State(b,self, m)
                successors+= [new_obj]
                
        return successors
        
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True

    def print_moves_to(self):
        """ Prints the sequence of moves that lead from the initial state
            to the called State object.
        """
        if self.predecessor == None:    # base case
            print('initial state:')
            print (self.board)
        else:
            self.predecessor.print_moves_to()
            print("move the blank",self.move + ":")
            print(self.board)
            
            # make a recursive call to print the moves to the predecessor state
            # print the move that led to self (see format below)
            # print the board associated with self