from typing import List
# Write any import statements here
import unittest
from collections import defaultdict
"""
Problem: given grid G which contains 1 and 0 representing 1 as battleship and 0 means empty. Find a probability of hitting battle ship 
Solution Approach:
simple count the 1s and 0s and return the 1s/total

Pseudo Code:
initialize the Counter, loop through the Grid and count both 1s and 0s
return 1s / (1s + 0s)

Time Complexity : O(R * C) looping through grid length
Space Complexity: O(1) two values of 1s and 0s in Counter
"""
def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  count = defaultdict(float)
  for i in range(R):
    for j in range(C):
      count[G[i][j]] += 1.0
      
  
  return count[1] / (count[1] + count[0])


class TestSolution(unittest.TestCase):
  def test_given_cases(self):
    self.assertEqual(getHitProbability(2,3,[[0,0,1],[1,0,1]]), 0.5)
    self.assertEqual(getHitProbability(2,2,[[1,1],[1,1]]), 1.0)


if __name__ == '__main__':
  unittest.main()