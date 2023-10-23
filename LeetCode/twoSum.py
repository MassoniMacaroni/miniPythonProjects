# LeetCode 1. Two Sum
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        numsLength = len(nums)
        while index < numsLength:
            for indexOfNums, number in enumerate(nums):
                if (number + nums[index]) == target and index != indexOfNums:
                    answerArray = [indexOfNums, index]
                    return answerArray
            index += 1
            
    
    testAnswer = [3,2,4]
    print (twoSum("self",testAnswer,6))
    
    #I'm not happy with this solution but I'm trying to work on consistently completing an LC problem a day before I revise better solutions