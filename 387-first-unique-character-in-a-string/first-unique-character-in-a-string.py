class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = {}
        for item in s:
            if item in dict1:
                dict1[item] +=1
            else:
                dict1[item] = 1
        i = 0
        for idx, char in enumerate(s):
            if dict1[char] == 1:
                return idx

        return -1
        