from cgi import test
from venv import create

# Done as a practice coding problem :)

class Solution:

    """Class for performing the 'count and say' recursion, where integers are 'said' and then turned back into integers. E.g. 1211 is 'said' '1 one, 1 two, 2 ones', and would then be converted to 111221."""

    def countandsay(self, n):

        """Main method in class. Performs the recursion n-1 times and returns the string version of the final result."""
        
        said_number = 1
        # Perform n-1 interations
        for iteration in range(n-1):

            # Convert to list of pairs and then convert back
            listed_pairs = makepairs(str(said_number))
            said_number = createint(listed_pairs)

        # Outputs the number as a string
        return said_number

    def makepairs(self, number: str):
        
        """Helper method for countandsay. Takes in integer (as a string) and converts it into a list of pairs in which each pair hold the number of each number."""
        
        # Set up counters and holders for loop
        curr_num = number[0]
        counter = 1
        pairs = []

        # Add pairs to list when necessary
        for digit in range(1, len(number)):
            if number[digit] != curr_num:
                pairs.append([counter, int(curr_num)])
                counter = 1
                curr_num = number[digit]
            else:
                counter += 1

        # Add final pair and return
        pairs.append([counter, int(curr_num)])
        return pairs

    def createint(self, created_pairs: list):

        """Helper method for countandsay. Takes a list of pairs and converts it back into an integer."""

        # Empty string for storage of new integer
        new_int = ""

        # Add each part of pair and return result
        for subpair in created_pairs:
            new_int = new_int + str(subpair[0])
            new_int = new_int + str(subpair[1])
        return int(new_int)


