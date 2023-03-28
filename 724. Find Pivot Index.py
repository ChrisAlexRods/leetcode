class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums) # O(n)
        leftSum =  0

        for num in range(len(nums)):
            rightSum = total - nums[num] - leftSum
            if leftSum == rightSum:
                return num
            leftSum += nums[num] # if it isn't the pivot index add it
        return -1 # if not pivot index make it -1 as per question