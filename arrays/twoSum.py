class twoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[n] = i
        
        return None

# T O(n), S O(n) 

# NAIVE 
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if (nums[i] + nums[j] == target):
#                     return [i, j]
# T O(n^2), S O(1)