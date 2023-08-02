#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Rashfiqur Rahman
# email: rash@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Wasay Rizwan
# partner's email: wasayr1@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        count = 0
        for x in range(3):
            for y in range(3):
                self.tiles[x][y] = digitstr[count]
                if digitstr[count] == '0':
                    self.blank_r = x
                    self.blank_c = y
                count+=1
        # Do *NOT* remove our code above.


    ### Add your other method definitions below. ###
    #Function2
    def __repr__ (self):
        """returns a string representation of a Board object
        """
        s= ''
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] == "0":
                    s+= "_"
                else:
                    s+= self.tiles[row][col]
                s+= " "
            s+= "\n"
        return s
    #Function 3
    def move_blank (self, direction):
        """takes as input string direction and returns True or False
        if the move in the requested direction is possible
        """
        new_row = self.blank_r
        new_col = self.blank_c
        if direction == "up":
            new_row -=1
        elif direction =="down":
            new_row+=1
        elif direction =="left":
            new_col-=1
        elif direction =="right":
            new_col+=1
        if (new_col<0 or new_col >2 or new_row<0 or new_row>2):
            return False
        else:
            self.tiles[self.blank_r][self.blank_c] = self.tiles[new_row][new_col]
            self.tiles[new_row][new_col] = "0"
            self.blank_r = new_row
            self.blank_c = new_col           
            return True
        return False           

    #Function 4
    def digit_string(self):
        """creates and returns a string representing the digits in the tile"""
        s = ''
        for r in range(3):
            for c in range(3):
                s+=self.tiles[r][c]
        return s 
    #Function 5
    def copy(self):
        """does a deep copy of the Board object"""
        copy_object = Board (self.digit_string())
        return copy_object
    #Function 6
    def num_misplaced (self):
        """counts and returns the number of tiles in the called
        Board object that are not where they should be in the 
        goal state"""
        count =0
        position =0
        perfect_str = '012345678'
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != perfect_str[position] and self.tiles[r][c] != "0":
                    count+=1
                position+=1
        return count
    #Function 7
    def __eq__(self, other):
        """this method is called when the == operator ius used to
        compare two Board objects. Returns True when the called
        object and the argument have same values
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False
        