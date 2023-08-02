#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Rashfiqur Rahman
# email: rash@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Wasay Rizwan
# partner's email: wasayr1@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__( self, init_depth_limit):
        """constructor for the Searcher class"""
        self.states = []
        self.num_tested = 0
        self.depth_limit = init_depth_limit

    
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    #Function 2
    def add_state(self, new_state):
        """takes a single State object called new_state and adds it
        the Searcher's list of untested states"""
        self.states +=[new_state]
    
    #Function 3
    def should_add(self, state):
        """takes a State object called state and returns True if the
        called Searcher should add state to its list of untested states 
        and False otherwise"""
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle() == True:
            return False
        else:
            return True     # no depth limit
        
    #Function 4
    def add_states(self, new_states):
        """takes a list of State objects called new_states, and that 
        processes the elements of new_states one at a time:"""
        for s in new_states:
            if self.should_add(s) == True:
                self.add_state(s)
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    def find_solution(self, init_state):
        """performs full state-space search that begins at the specified
        initial state init_state and ends when the goal state is found or 
        when the Searcher runs out of untested states"""
        self.add_state(init_state)
        while self.should_add(init_state) == True:
            s = self.next_state()
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
        return None
    
                
        
            


### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    
    def next_state(self):
        """ Overrides the next_state method that is inherited from Searcher.
            Rather than choosing at random from the list of untested states,
            this version of next_state should follow FIFO ordering - choosing
            the state that has been in the list the longest.
        """
        s = self.states[0]
        self.states.remove(s)
        return s
class DFSearcher(Searcher):
    
    def next_state(self):
        """ Overrides the next_state method that is inherited from Searcher.
            Should follow LIFO ordering.
        """
        s = self.states[-1]
        self.states.remove(s)
        return s
    
    
def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###



class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    
    def __init__(self, heuristic):
        """ Constructor for a new GreedySearcher object
        """
        super().__init__(-1)
        self.heuristic = heuristic
    def add_state(self, state):
       """overrides the add_state method that is inherited from Seacher"""
       new_list =[]
      
       new_list += [self.priority(state), state]
       self.states += [new_list]
    def next_state(self):
        """overrides the next_state method that is inherited from Searcher"""
        greatest_priority = max(self.states)
        self.states.remove(greatest_priority)
        return greatest_priority[1]
  
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

def h1(state):
    """takes a State object called state and that computes and returns
    an estimate of how many additional moves are needed to get from
    state to the goal state."""
    return state.board.num_misplaced()
    
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
class AStarSearcher(GreedySearcher):
    """class for searcher objects that perform A* search. It is informed search algorithm
    """
    
    def priority(self, state):
        """replaces the priority method from Greedy. The priority is
        computed by the heuristic function and the number of moves"""
        
        return (-1 * (self.heuristic(state) + state.num_moves))
        
   
        
### Add your AStarSeacher class definition below. ###
