#Leetcode 1929. Concatenation of Array
from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        print(numsLength)
        concatArray = [0 for i in range(2*numsLength)]
        for indexOfNums, number in enumerate(nums):
            print(indexOfNums, number)
            concatArray[indexOfNums] = number
            concatArray[indexOfNums + numsLength] = number
        print(concatArray)
        return concatArray
    
    input = [1,2,1]
    getConcatenation("self", input)