from typing import List
import unittest
# Write any import statements here
"""
Understanding Problem:
minimum no. of distinct problem solved in the contest provided by competitors scores

Example:
[1,2,4,6,8,9] 9 // 2 = 4 + 1 = 5
[1,3,5,7,10] 10/ 5 = 5 => 4 + 1 + 1 = 6

pseudo code

find max val from the list 
if max is even 
  check if odd exist in the list
  ( max / 2 ) - 1 + 2
else:
  max // 2 + 1
  
Time complexity O(N) to check odd + finding max
Space complexity O(1)
"""
def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  count = 0
  max_val = max(S)
  if max_val % 2 == 0:
    count = max_val / 2
    if any(num % 2 != 0 for num in S):
      count = count + 1
  else:
    count = (max_val // 2) + 1
    
  return count

class TestSolution(unittest.TestCase):
  def test_given_cases(self):
    self.assertEqual(getMinProblemCount(6, [1,2,3,4,5,6]), 4)
    self.assertEqual(getMinProblemCount(4, [4,3,3,4]), 3)
    self.assertEqual(getMinProblemCount(4, [2,4,6,8]), 4)


if __name__ == '__main__':
  unittest.main()