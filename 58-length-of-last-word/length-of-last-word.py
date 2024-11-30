class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_len = 0
        begin = False
        for char in s[::-1]:
            if char == ' ' and not begin:
                begin = True
            elif char != ' ':
                begin = True
                last_len +=1
            elif char == ' ' and last_len >0:
                return last_len
            
            

        return last_len
