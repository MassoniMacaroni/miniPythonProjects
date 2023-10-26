#Leetcode 1929. Concatenation of Array
from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concatArray = []
        for i in range(2):
            for number in nums:
                concatArray.append(number)
        return concatArray
    input = [1,2,1]
    getConcatenation("self", input)