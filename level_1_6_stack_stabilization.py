from typing import List
import unittest
# Write any import statements here
"""
understanding the problem:
We need to deflate the disk radious to stablize the stack. the stack can be any order
Example: [5,3,4,5,8] 
in order to deflate, I need to see the bottom piece first 
add all of them stake, pop one a time and add it back to the list 8,5,4,3,2 
count the deflated ponits
[2,5,3,6,5] => read from back 5, 4, 3, 2, 1 count 3

pseduo code:
initialize count
reverse loop (n-2, -1, -1)
  check last two deflate
    count +=
    check if deflated < 1 then
      return -1
  return count
  
  
Time complexity O(n) n is the length of the string
space complexity O(1)
"""

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # Write your code here
  if N <= 1:
    return 0
  
  count = 0
  for i in range(N-2,-1, -1):
    if R[i] >= R[i+1]:
      R[i] = R[i] - (R[i] - R[i+1] + 1)
      if R[i] < 1:
        return -1
      count += 1
  return count

class TestSolution(unittest.TestCase):
  def test_given_cases(self):
    self.assertEqual(getMinimumDeflatedDiscCount(5,[2,5,3,6,5]), 3)
    self.assertEqual(getMinimumDeflatedDiscCount(3, [100,100,100]), 2)
    self.assertEqual(getMinimumDeflatedDiscCount(4,[6,5,4,3]), -1)


if __name__ == '__main__':
  unittest.main()
