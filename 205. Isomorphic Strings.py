class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if ((c1 in mapST and mapST[c1] != c2) or
            (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True

# This code defines a class called Solution that has a single method isIsomorphic. The method checks whether two input strings s and t are isomorphic or not. Two strings are isomorphic if the characters in one string can be replaced with characters in another string to get the second string. In other words, there is a one-to-one mapping between the characters of the first string and the characters of the second string.

# The isIsomorphic method does the following:

# Create two empty dictionaries, mapST and mapTS. They will store the mappings between the characters in the strings s and t, respectively.

# Iterate through the characters in the input strings s and t using their indices (variable i).

# For each character pair (c1, c2) from strings s and t, check if:
# a. c1 is already in mapST and the value stored for this key is not equal to c2.
# b. c2 is already in mapTS and the value stored for this key is not equal to c1.
# If either of these conditions is true, return False, as the strings are not isomorphic.

# If the conditions in step 3 are not met, update the mappings in both dictionaries:
# a. Set the value of key c1 in mapST to c2.
# b. Set the value of key c2 in mapTS to c1.

# If the loop completes without finding any violations, return True, as the strings are isomorphic.