'''
Problem Statement:

You are given two non-empty linked lists representing two non-negative integeers. The digits are stoerd in reverse order, and each of their 
nodes contains a single digit. Add the twoo numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(max*m,n)) Time Complexity
    # O(1) Space Complexity
    # ! Scuffed Solution
        def addTwoNumbers(self, l1, l2):
            flag_l1 = False
            flag_l2 = False
            
            root = ListNode()
            curr_node = root

            while(1==1):
                curr_node.val += l1.val + l2.val

                if l1.next != None:
                    l1 = l1.next
                else:
                    # print('Trip l1')
                    l1.val = 0
                    flag_l1 = True
                    
                if l2.next != None:
                    l2 = l2.next
                else:
                    # print('Trip l2')
                    l2.val = 0
                    flag_l2 = True

                temp_node = ListNode()
                if curr_node.val > 9:
                    temp_node.val = 1
                    curr_node.val = curr_node.val % 10

                if flag_l1 and flag_l2:
                    # print('Trigger')
                    if temp_node.val == 1:
                        curr_node.next = temp_node
                    return root
                curr_node.next = temp_node
                curr_node = temp_node

            

            return root
        
    # O(max*m,n)) Time Complexity
    # O(1) Space Complexity
    # ! TODO CARRY SOLUTION
        def addTwoNumbers(self, l1, l2):
            flag_l1 = False
            flag_l2 = False
            
            root = ListNode()
            curr_node = root

            while(1==1):
                curr_node.val += l1.val + l2.val

                if l1.next != None:
                    l1 = l1.next
                else:
                    # print('Trip l1')
                    l1.val = 0
                    flag_l1 = True
                    
                if l2.next != None:
                    l2 = l2.next
                else:
                    # print('Trip l2')
                    l2.val = 0
                    flag_l2 = True

                temp_node = ListNode()
                if curr_node.val > 9:
                    temp_node.val = 1
                    curr_node.val = curr_node.val % 10

                if flag_l1 and flag_l2:
                    # print('Trigger')
                    if temp_node.val == 1:
                        curr_node.next = temp_node
                    return root
                curr_node.next = temp_node
                curr_node = temp_node

            

            return root
        

    
    
# <--------------------------- Main --------------------------->
    
def main():
    Agent = Solution()
    
    l1 = [2,4,3]
    l2 = [3,6,4]
    
    ll1_head = ListNode()
    ll2_head = ListNode()
    
    ll1 = ll1_head
    ll2 = ll2_head
    
    for num in l1:
        ll1.val = num
        
        next_node = ListNode()
        ll1.next = next_node
        ll1 = next_node
        
    for num in l2:
        ll2.val = num
        
        next_node = ListNode()
        ll2.next = next_node
        ll2 = next_node
    
    result = Agent.addTwoNumbers(ll1_head,ll2_head)
    
    print(result)

# This function checks if the current script being run is the main program
if __name__ == "__main__":
    main()