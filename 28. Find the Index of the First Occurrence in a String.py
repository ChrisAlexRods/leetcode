# 28. Find the Index of the First Occurrence in a String
# Easy
# 3.4K
# 179
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


# In Python, you can use the built-in find() function of string objects to solve this problem. The find() function
# returns the index of the first occurrence of the specified value, or -1 if the value is not found.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

solution = Solution()
print(solution.strStr("sadbutsad", "sad"))  # 0
print(solution.strStr("leetcode", "leeto"))  # -1
