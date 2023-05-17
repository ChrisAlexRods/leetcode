# 58. Length of Last Word
# Easy
# 3.1K
# 163
# Companies
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
#  consisting of non-space characters only.



# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


# Your current implementation isn't correct because s[-1] gives you the last character of the string,
# not the last word. To find the last word, you can use the split() function, which breaks the string
# into a list of words. Here's the corrected code:

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()

        if not words:
            return 0
        return len(words[-1])


solution = Solution()
print(solution.lengthOfLastWord("Hello World"))  # 5
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # 4
print(solution.lengthOfLastWord("luffy is still joyboy"))  # 6
print(solution.lengthOfLastWord(" "))  # 0
