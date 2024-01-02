'''
Problem Description:

You are given an integer array numbs. You need to create a 2D array from numbs satisfying the following conditions:
 * The 2D array should contain only the elements of the array numbs.
 * Each row in the 2D array contains distinct integers
 * The number of rows in the 2D array should be minimal
 
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D aray can have a different number of elements on each row

https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
'''

class Solution:
    # O(N) Time Complexity
    # O(N) Space Complexity
    # ! First Solution (frequency counter)
    # Solution Summary = use dictionaries to check for distinct integers, either convert them into the lists at the end, or maintain lists along with them
    
    def findMatrix(self, nums):
        # use single dictionary with num of occurences to know where to place the number within matrix
        distinct_counts = dict()
        
        matrix = []
        
        for num in nums:
            # check if number is distinct, if it is, increment its occurences
            if num not in distinct_counts:
                distinct_counts[num] = 0
            distinct_counts[num] += 1
            
            # add number to the matrix
            # print(f'Occurences of {num} are {distinct_counts[num]}')
            if len(matrix) < distinct_counts[num]:
                matrix.append([num])
            else:
                matrix[distinct_counts[num]-1].append(num)
                
        return matrix

# <--------------------------- Main --------------------------->
    
def main():
    Agent = Solution()
    
    ex_1 = [1,2,3,1,4,2,5,3,1,1,2,3,1,1,1]
    
    result = Agent.findMatrix(ex_1)
    
    print(result)
    
    return

# This function checks if the current script being run is the main program
if __name__ == "__main__":
    main()