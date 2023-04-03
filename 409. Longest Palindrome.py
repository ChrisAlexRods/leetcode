class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Create a dictionary to store the frequency of each character in the string
        char_freq = {}

        # Iterate through the string and count the frequency of each character
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        # Initialize variables to keep track of the length of the longest palindrome and if there's an odd frequency character
        longest_palindrome_length = 0
        has_odd_frequency = False

        # Iterate through the character frequencies
        for freq in char_freq.values():
            # If the frequency is even, add it directly to the palindrome length
            if freq % 2 == 0:
                longest_palindrome_length += freq
            else:
                # If the frequency is odd, add the largest even number smaller than the frequency to the palindrome length
                longest_palindrome_length += (freq // 2) * 2
                # Set the has_odd_frequency flag to True
                has_odd_frequency = True

        # If there's at least one character with odd frequency, we can add it to the center of the palindrome, so increment the length by 1
        if has_odd_frequency:
            longest_palindrome_length += 1

        return longest_palindrome_length
