class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dict1 = { key: False for key in range(1,len(nums)+1)}
        for num in nums:
            dict1[num] = True

        disappeared = [key for key,value in dict1.items() if not value]
        return disappeared