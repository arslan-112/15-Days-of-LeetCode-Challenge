class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_len = 0
        
        for char in s[::-1]:  
            if char != ' ':  
                last_len += 1
            elif last_len > 0:  
                return last_len
        return last_len  
            
            

    