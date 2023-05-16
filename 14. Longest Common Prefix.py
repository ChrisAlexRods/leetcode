# 14. Longest Common Prefix
# Easy
# 13.8K
# 3.9K
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".



# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # find the shortest string in the list
        shortest = min(strs, key=len)
         # iterate over each character in the shortest string
        for i, char in enumerate(shortest):
            # iterate over each string in the list
            for other in strs:
                 # if the current character does not match the corresponding character in another string,
                 # return the prefix up to this point
                if other[i] != char:
                    return shortest[:i]
        # if we made it through all the characters in the shortest string without finding a mismatch,
        # the whole shortest string is the common prefix
        return shortest


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))  # prints "fl"
print(s.longestCommonPrefix(["dog","racecar","car"]))  # prints ""


# This function works by first finding the shortest string in the list, because the common prefix cannot
# be longer than the shortest string. It then checks each character in the shortest string against the corresponding
# character in all the other strings. As soon as it finds a character that is not the same in all strings, it returns the
# prefix up to that point. If it makes it through all the characters in the shortest string without finding a mismatch, it
# returns the whole shortest string as the common prefix.