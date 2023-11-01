class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if target == nums[i] + nums[j]:
                    return (i,j)

        return
    
    
def main():
    
    return

# __name__ is a special variable name in python, when this python script is run directly, the value will change to __main__
# This function checks if the current script being run is the main program
if __name__ == "__main__":
    main()