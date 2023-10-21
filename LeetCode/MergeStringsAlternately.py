#Leetcode 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1Length = len(word1)
        word2Length = len(word2)
        combinedLength = word1Length + word2Length
        
        newString = ""
        i = 0
        while i < combinedLength:
            if i < word1Length:
                newString += word1[i]
            if i < word2Length:
                newString += word2[i]
            
            i += 1
        
       
        return newString
    
    mergeAlternately("self", "abc", "defdd")

