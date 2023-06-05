class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for i in nums:
            total += i
            result.append(total)
        return result

#The result was a list, the adding is happening inside the list.

def test_runningSum():
    solution = Solution()

    assert solution.runningSum([1,2,3,6,8,9]) == [1,3,6,10], "Test Case 1 Failed"
    assert solution.runningSum([1,1,1,1,1]) == [1,2,3,4,5], "Test Case 2 Failed"
    assert solution.runningSum([3,1,2,10,1]) == [3,4,6,16,17], "Test Case 3 Failed"
    assert solution.runningSum([-1,2,-3,4]) == [-1,1,-2,2], "Test Case 4 Failed"
    assert solution.runningSum([]) == [], "Test Case 5 Failed"

    print("All test cases pass")

if __name__ == "__main__":
    test_runningSum()
