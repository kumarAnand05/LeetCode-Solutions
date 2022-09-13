class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for n in range(len(nums)):
            for m in range(n+1,len(nums)):
                if nums[n]+nums[m]== target:
                    return [n, m]
                    break

"""
The above problems takes custom input for pre-defined variables for function 'twoSum':
  1. nums- takes input in list type and contains int
  2. target- takes input in int format
  RETURN value of twoSum function should be of list type with int data type stored.

  The following problem is solved using two nested loops:
    The first loop iterate through list from start to end.
      The second loop iterates for each value of loop 1 from that elemnt to end elemnet.
       Conditional statement check if the sum of the number being iterated in loop1 and loop2 is equal to target or not,
       in case it's not true then loop 2 loops till end. If no element found then the loop1 picks the other element and repeates again.
       When conditional statement is true the function retuns the value of respetive indices.

"""