class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] = nums[i]**2
            
        i = 0
        j = len(nums) -1
        squares = [0] *len(nums)
        for x in range(len(nums)-1,-1,-1):
            if nums[i] > nums[j]:
                squares[x] = nums[i]
                i+=1
            else:
                squares[x] = nums[j]
                j-=1
        return squares



        