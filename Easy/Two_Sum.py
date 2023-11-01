class Solution:
    # O(n^2) Time Complexity
    # O(1) Space Complexity
    # ! INEFFICIENT solution
    def twoSum(self, nums, target):
        '''
        Explanation of Solution:
        
        simple double loop solution
        
        '''
        
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if target == nums[i] + nums[j]:
                    return (i,j)

        return
    
    # O(n) Time Complexity
    # O(n) Space Complexity
    # ! Double Pass Hash Table solution
    def twoSumBetter(self, nums, target) :
        '''
        Explanation of Solution:
        
        This solution uses a hash table to quickly identify if the target exists:
        1. Place all list values in a dictionary where the key is the number, and the value is the index
        2. Loop through all indexes of i, checking if target minus current list value exists within the hash_table
            a. I also check to make sure the current value doesn't use itself in the hash table
        3. If the value exists as a key, and the value is not the current list element, then return their indexes
        '''
        
        hash_table = dict()

        # Target = x + y
        # Target - x = y

        for i in range(len(nums)):
            hash_table[nums[i]] = i

        for i in range(len(nums)):
            # print(nums[i])
            
            key = target - nums[i]
            # print('Key:', key)
            
            # 
            if key in hash_table and hash_table[key] == i:
                continue

            if key in hash_table:
                # print("Found!")
                return (i,hash_table[key])

        return
    
    # O(n) Time Complexity
    # O(n) Space Complexity
    # ! Single Pass Hash Table solution
    def twoSumBest(self, nums, target) :
        '''
        Explanation of Solution:
        
        This solution uses a hash table to quickly identify if the target exists:
        1. Place all list values in a dictionary where the key is the number, and the value is the index
        2. Loop through all indexes of i, checking if target minus current list value exists within the hash_table
        3. If the value exists as a key, then return their indexes
        
         * This solution does not require us to check if the list value's index is the same as the current values's index because the element has not been inserted into the hash map yet
        '''
        
        hash_table = dict()

        # Target = x + y
        # Target - x = y

        for i in range(len(nums)):
            y = target - nums[i]
            
            if y in hash_table:
                return (i,hash_table[y])
            
            hash_table[nums[i]] = i

        return
    
        # O(n) Time Complexity
    # O(n) Space Complexity
    # ! Single Pass Hash Table solution
    def twoSumBestAlt(self, nums, target) :
        '''
        Explanation of Solution:
        
        This solution uses a hash table to quickly identify if the target exists:
        1. Place all list values in a dictionary where the key is the number, and the value is the index
        2. Loop through all indexes of i, checking if the compliment exists, if so return the curr index and hash_table value index
        '''
        
        hash_table = dict()
        
        for i in range(len(nums)):

            # Target = x + y
            # Target - x = y
            
            print('Curr Num:', nums[i])
        
            if nums[i] in hash_table:
                print("Found!")
                
                return (i, hash_table[nums[i]])

            # print('Compliment:',target-nums[i])
            key = target-nums[i]
            hash_table[key] = i

        return
    
    
    
    
def main():
    Agent = Solution()
    
    test_list = [2,5,5,11]
    target = 10
    
    result = Agent.twoSum(test_list, target)
    
    print(result)
    
    result = Agent.twoSumBetter(test_list, target)
    
    print(result)
    
    result = Agent.twoSumBest(test_list,target)
    
    print(result)
    
    result = Agent.twoSumBestAlt(test_list,target)
    
    print(result)
    
    return

# __name__ is a special variable name in python, when this python script is run directly, the value will change to __main__
# This function checks if the current script being run is the main program
if __name__ == "__main__":
    main()