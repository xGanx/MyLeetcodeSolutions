'''
Problem Description:

Given a string s, find the length of the longest substring without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    # O(N) Time Complexity
    # O(N) Space Complexity
    # ! First Solution
    # Solution Summary = loop through s, use hashset to save indeces of characters and check for dups
    
    def lengthOfLongestSubstring(self, s):
        seen = dict()
        beg_index = 0
        longest_substring = 0
        
        for i, letter in enumerate(s): # use enumeration to loop through all chars and maintain an index variable
            if seen.get(letter, -1) >= beg_index: # forgot this function exists for dictionaries in python
                beg_index = seen[letter] + 1 # cutoff first occurrence
            longest_substring = max(longest_substring, i - beg_index + 1)
            seen[letter] = i # leave the second occurrence in the substring
        
        return longest_substring
    
    
# <--------------------------- Main --------------------------->
    
def main():
    
    Agent = Solution()
    s = 'aaabbasd'
    result = Agent.lengthOfLongestSubstring('aab')
    
    print(result)
    
    return

# This function checks if the current script being run is the main program
if __name__ == "__main__":
    main()