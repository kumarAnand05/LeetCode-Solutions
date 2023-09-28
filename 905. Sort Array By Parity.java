class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int arr[]=new int[nums.length];
        int f=0;
        int b=nums.length-1;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]%2==0)
            {
                arr[f++]=nums[i];
            }
            else
            {
                arr[b--]=nums[i];
            }
        }
        return arr;       
    }
}
