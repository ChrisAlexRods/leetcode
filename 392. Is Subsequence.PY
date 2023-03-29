class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: #o(n)
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1 #These move the pointers and increment
            j += 1 #These move the pointers and increment
        return True if i == len(s) else False

# There is two pointers we're using to compare each character in the s string to the t string.
#the while loops keeps it so that it keeps looping until the we reach the length of s and t

#Inside the loop, if the characters at the current indices "i" and "j" are the same (s[i] == t[j])
# , the index "i" is incremented. Regardless of whether the characters match, the index "j" is incremented at the end of each iteration.

#When the loop ends, if the index "i" is equal to the length of string "s" (i == len(s)),
# it means that all characters in "s" have been matched in "t" while maintaining their order, and hence "s" is a subsequence of "t".

# The if statement is checking if they're the same and if they are we adjust the main i pointer
# if not we keep the i pointer and adjust the j pointer instead
# The return statement i a little weird but if the i pointer