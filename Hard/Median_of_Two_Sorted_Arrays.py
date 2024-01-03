'''
Problem Description:

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Odd Numbers Case:   Median of 1,2,3 = 2
Even Numbers Case:  Median of 1,2,3,4 = 2.5 because (2+3) / 2 = 5 / 2 = 2.5

https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

# collections.deque is better for performacne in single threaded cases
# queue.Queue is better for concurrency cases
from collections import deque

class Node: # quick note that private variabels and methods are denoted by a __ in python
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def __str__(self):
        return f'{self.data}'

class BinaryTree: 
    
    def __init__(self, root=None):
        self.root = root
        
    # Private helper function used to find nodes, returns as False if node cannot be found
    def __findNode(self, data, cursor):
        if cursor.data == data:
            return cursor
        else:
            if data < cursor.data:
                if cursor.left:
                    return self.__findNode(data, cursor.left)
                return False
            else:
                if cursor.right:
                    return self.__findNode(data, cursor.right)
                else:
                    return False
            
        
    # Default insert based on sorting lesser than values to the left and greater than values to the right
    def insert(self, data): # cursor is the root node of the binary search tree (starts at root node)
        # Base case where the root is None type
        if self.root == None: 
            self.root = Node(data)
        else:
            self.__insert(data, self.root)
            
    def __insert(self, data, cursor):
        if data < cursor.data:
            if cursor.left:
                cursor.left = Node(data)
            else:
                self.__insert(data, self.root)
        else:
            if cursor.right:
                cursor.right = Node(data)
            else:
                self.__insert(data, self.root)
                
        
            
    # Return false if delete unsuccessful
    def delete(self, data):
        if self.root == None:
            return -1
        else:
            node = self.__findNode(data, self.root)
            if node:
                node = None
                return True
            else:
                return False
            
    def deleteTree(self):
        self.root = None
        return True
            
    # Return false if element does not exist
    def get(self, data):
        if self.root == None:
            return False
        else:
            return self.__findNode(data, self.root)
    
    # Calculates the depth of the tree to a node if specified, otherwise, returns tree depth
    def getDepth(self, data=None): # use bfs to find depth (node, depth)
        if self.root == None:
            return -1
        
        q = deque()
        q.append((self.root,0))
        
        if data is not None:            
            while len(q) > 0: # note 'is' and '==' differ, is checks if the variables point to the same object in memory, == checks for equality
                node = q.pop() # tuple (node, depth)
                if node[0].data == data:
                    return node[1]
                else:
                    if node[0].left:
                        q.append((node[0].left), node[1]+1)
                    if node[0].right:
                        q.append((node[0].right), node[1]+1)  
            return -1 # Signifies the node was not found            
        else:
            max_depth = 0
            
            while len(q) > 0:
                node = q.pop() # tuple (node, depth)
                if node[1] > max_depth:
                    max_depth = node[1]
                else:
                    if node[0].left:
                        q.append((node[0].left), node[1]+1)
                    if node[0].right:
                        q.append((node[0].right), node[1]+1)  
    
    def getInOrder(self, node):
        print(self.getInOrder(node.left()))
        print(node.data())
        print(self.getInOrder(node.right()))
        return
    
    def getPreOrder(self, node):
        print(node.data())
        print(self.getInOrder(node.left()))
        print(self.getInOrder(node.right()))
        return
    
    def getPostOrder(self, node):
        print(self.getInOrder(node.left()))
        print(self.getInOrder(node.right()))
        print(node.data())
        return
    
    def getLevelOrder(self, node):
        q = deque()
        q.append((self.root))
        while(len(q) > 0):
            node = q.pop()
            print(node.data)
            if node.left():
                q.append(node.left)
            if node.right():
                q.append(node.right)
        return
        
    def isEmpty(self):
        return self.root == None
        
    def __str__(self):
        return f'Binary Tree: {self.root}'
        
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
    # print(b_tree)
    # print(a)
    
    e = Node(7)
    
    print(BinaryTree())
    
    b_tree.insert(8)
    print(b_tree)
    
    
    # AVL Tree Testing Stuff
    
    return

# This function checks if the current script being run is the main program
if __name__ == "__main__":
    main()