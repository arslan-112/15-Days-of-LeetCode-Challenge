class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        for key,val in nums_dict.items():
            if val > len(nums)//2:
                return key
        