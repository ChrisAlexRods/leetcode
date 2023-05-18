# 67. Add Binary
# Easy
# 8K
# 785
# Companies
# Given two binary strings a and b, return their sum as a binary string.



# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# Let's go through the examples to understand the problem better:

# Example 1:

# Input: a = "11", b = "1"

# "11" is binary for 3 and "1" is binary for 1. If you add 3 and 1, you get 4, which is "100" in binary. So the output is "100".

# Example 2:

# Input: a = "1010", b = "1011"

# "1010" is binary for 10 and "1011" is binary for 11. If you add 10 and 11, you get 21, which is "10101" in binary. So the output is "10101".

# In Python, you can use the int() function with base 2 to convert a binary string to an integer. Then, you can perform the addition operation, and finally, use the bin() function to convert the result back to a binary string. The bin() function returns a string that starts with "0b", so you need to remove this prefix using slice notation.

# Here's the corrected Python code:

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_a = int(a, 2)
        int_b = int(b, 2)

        sum_ab = int_a + int_b

        binary_sum_ab = bin(sum_ab)

        return binary_sum_ab[2:]

solution = Solution()
print(solution.addBinary("11", "1"))  # "100"
print(solution.addBinary("1010", "1011"))  # "10101"
