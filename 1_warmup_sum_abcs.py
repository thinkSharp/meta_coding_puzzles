import unittest
"""
Problem:
Given three integers (A,B,C) determine their sum.
Your task is to implement the function getSum(A, B, C) which returns the sum 

Solution Approach.
Simply Add three given values and return the output

Time complexity O(1)
Space Complexity O(1)
"""
def getSum(A: int, B: int, C: int) -> int:
    return A + B + C

class TestCases(unittest.TestCase):
    def test_given_cases(self):
        self.assertEqual(getSum(1,2,3), 6)
        self.assertEqual(getSum(100,100,100), 300)
        self.assertEqual(getSum(85,16,93), 194)


if __name__ == '__main__':
    unittest.main()

    