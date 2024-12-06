class Solution {
    public int maxSubArray(int[] nums) {
        int maxSub = nums[0];
        int currsum = 0;
        for(int i=0; i<nums.length; i++){
            if(currsum < 0)
                currsum = 0;
            currsum += nums[i];
            if(currsum > maxSub)
                maxSub= currsum;
        }
        return maxSub;

    }
}