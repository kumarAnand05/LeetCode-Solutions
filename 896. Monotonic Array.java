class Solution {
    public boolean isMonotonic(int[] nums) {
        int firstEl=nums[0];
        int lastEl=nums[nums.length-1];

        if (firstEl<lastEl)
        {
            for(int i=0;i<nums.length-1;i++)
            {
                if(nums[i]>nums[i+1])
                {
                    return false;
                }
            }
        }

        else
        {
            for(int i=0;i<nums.length-1;i++)
            {
                if(nums[i]<nums[i+1])
                {
                    return false;
                }

            }
        }
        return true;
    }
}
