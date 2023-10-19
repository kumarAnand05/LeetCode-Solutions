/*
Question:

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
*/

// Solution:

class Solution {
    public int numIdenticalPairs(int[] nums) {
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        int res=0;
        int sameCount=1;
        for(int i=0;i<nums.length-1;i++){
            if(i!=nums.length-1&&(nums[i]==nums[i+1])){
                sameCount+=1;
            }
            else
            {
                res+=(sameCount*(sameCount-1))/2;
                sameCount=1;
            }
        }
        res+=(sameCount*(sameCount-1))/2;
        return res;
    }
}
