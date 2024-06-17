class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, n = 0, 0, len(nums)

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1

        for i in range(zeros):
            nums[i] = 0
    
        for j in range(zeros, zeros+ones):
            nums[j] = 1
        
        for k in range(zeros+ones, n):
            nums[k] = 2

# T O(n), S O(1)