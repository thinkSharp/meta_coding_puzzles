from typing import List
# Write any import statements here
import unittest
from collections import OrderedDict
"""
Understanding the Problem:
1. a user can eat as many dishes as it can as long as they are not repeating to previous K dishes

Example:
[1,2,3,2,1,3,4,3,6,7] , K = 2
1,2,3
2,3 => skip 2 eat 1
3,1 -> skip 3 eat 4
1,4 -> eat 3,6,7 ==> 8

pseudo code
queue = deque() # K
for i in range(N):
  if i not in queue:
    count += 1
    queue.append(i)
    if len(queue) > K:
      queue.popleft()
 return count
 
 
Time complexity: O(n + K)
Space complexity: O(K)
"""
def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  if N == 0:
    return 0
  
  k_items = OrderedDict()
  count = 0
  for i in range(N):
    if D[i] not in k_items:
      count += 1
      k_items[D[i]] = True
      if len(k_items) > K:
        k_items.popitem(last=False)
        
  return count

class TestSolution(unittest.TestCase):
  def test_given_cases(self):
    self.assertEqual(getMaximumEatenDishCount(6,[1,2,3,3,2,1], 1), 5)
    self.assertEqual(getMaximumEatenDishCount(6,[1,2,3,3,2,1], 2), 4)
    self.assertEqual(getMaximumEatenDishCount(7,[1,2,1,2,1,2,1], 2), 2)


if __name__ == '__main__':
  unittest.main()