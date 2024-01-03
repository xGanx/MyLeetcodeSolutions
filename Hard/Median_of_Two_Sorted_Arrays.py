'''
Problem Description:

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Odd Numbers Case:   Median of 1,2,3 = 2
Even Numbers Case:  Median of 1,2,3,4 = 2.5 because (2+3) / 2 = 5 / 2 = 2.5

https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

class Node: # quick note that private variabels and methods are denoted by a __ in python
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    # Will print out recursively the data in the Nodes
    def __str__(self):
        return f'Data: {self.data} - Left Node: {self.left} - Right Node: {self.right}'

class BinaryTree: 
    
    def __init__(self, root=None):
        self.root = root
        
    def insert(self, data):
        return
    
    def delete(self, data):
        return
    
    def get(self, data):
        return
    
    def getHeight(self):
        return
    
    def getDepth(self):
        return
    
    def getInOrder(self):
        return
    
    def getPreOrder(self):
        return
    
    def getPostOrder(self):
        return
    
    def getLevelOrder(self):
        return
        
    def __str__(self):
        return f'Root Node: {self.root}'
        
class AVLTree(BinaryTree):
    # pass # used when you do not want to add any other properties or methods to the class
    def __init__(self):
        print()
        
    def rebalance():
        return
    
    def __str__(self):
        return ''

class Solution:
    # O(x) Time Complexity
    # O(x) Space Complexity
    # ! First Solution
    '''
    Solution Thoughts:
     * Use a self balancing binary heap (red-black? AVL?) to find the median
     * Red-black Tree = Alternates between levels of red and black nodes which are used to reorganize and ensure that the tree is also APPROXIMATELY balanced, not perfect balancing
     * AVL Tree = self-balancing binary search tree, more strictly balanced than red-black trees - best used with pre-sorted data
     
     * There exists two cases for finding the median, even number of nums, and odd number of nums, this should be used to determine how I traverse the created AVL tree to calculate the median
     
     Links:
      * https://en.wikipedia.org/wiki/AVL_tree
      * https://betsybaileyy.github.io/AVL_Tree/
      * https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
      
    '''
    
    def findMedianSortedArrays(self, nums1, nums2):
        
        return 
    
    
# <--------------------------- Main --------------------------->
    
def main():
    Agent = Solution()
    
    # result = Agent.findMedianSortedArrays()
    
    # print(result)
    
    # Binary Tree Testing Stuff
    a = Node(3)
    b = Node(2)
    c = Node(1)
    
    a.left = b
    a.right = c
    
    d = Node(4)
    b.left = d
    
    b_tree = BinaryTree(a)
    print(b_tree)
    print(a)
    
    
    # AVL Tree Testing Stuff
    
    return

# This function checks if the current script being run is the main program
if __name__ == "__main__":
    main()