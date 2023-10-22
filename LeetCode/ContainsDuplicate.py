# 217. Contains Duplicate
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsLength = len(nums)
        sortedNums = sorted(nums)
        index = 1
        while index < numsLength:
            if sortedNums[index] != sortedNums[index - 1]:
                index += 1
            else:
                print (sortedNums[index])
                return True
            
        return False       
        
    
    
    nums = [1,2,3,4,2]
    containsDuplicate("self",nums)