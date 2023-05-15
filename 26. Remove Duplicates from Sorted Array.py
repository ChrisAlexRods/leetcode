# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
         # Initialize two pointers
        pointer1 = 0

        for pointer2 in range(1,len(nums)):
             # If the current number is different from the previous one
            if nums[pointer2] != nums[pointer1]:
                pointer1 += 1
                # Move the different number to the front
                nums[pointer1] = nums[pointer2]
        # Since pointer1 starts from 0, add 1 to get the correct count
        return pointer1 + 1

# This function works by iterating over the array with two pointers. When two consecutive numbers are different,
# it means we have found a new unique number. We then move this unique number to the position after the last unique
# number we found. We continue this process until we have moved all unique numbers to the front of the array. The final
# length of the array without duplicates is the index of the last unique number plus one (because index starts at 0).