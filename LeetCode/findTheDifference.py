# LeetCode 389. Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count = {}
        
        for char in t:
            char_count[char] = char_count.get(char, 0) + 1
            
        for char in s:
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]

        return list(char_count.keys())[0]
        
    
        