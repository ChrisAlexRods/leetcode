# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.



# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I': 1, "V": 5, "X":10, "L":50, "C": 100, "D":500, "M":1000}
        result = 0
        prev_value = 0
        for symbol in s:
            current_value = dict[symbol]
            if current_value > prev_value:
                result += current_value -2 * prev_value
            else:
                result += current_value
            prev_value = current_value
        return result


s = "LVIII"
solution = Solution()
print(solution.romanToInt(s))

#To summarize, the romanToInt function has a time complexity of O(n) because it iterates through the input string once and performs constant-time operations for each symbol.

def romanToInt(self, s: str) -> int:
    # Define a dictionary to map each Roman numeral symbol to its decimal value
    dict = {'I': 1, "V": 5, "X":10, "L":50, "C": 100, "D":500, "M":1000}

    # Initialize the result to 0 and the previous value to 0
    result = 0
    prev_value = 0

    # Iterate through each symbol in the input string
    for symbol in s:
        # Look up the decimal value of the current symbol in the dictionary
        current_value = dict[symbol]

        # If the current value is greater than the previous value, subtract twice the previous value
        if current_value > prev_value:
            result += current_value -2 * prev_value
        # Otherwise, add the current value to the result
        else:
            result += current_value

        # Update the previous value to be the current value for the next iteration
        prev_value = current_value

    # Return the final result
    return result
