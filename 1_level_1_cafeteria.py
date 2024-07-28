from typing import List
# Write any import statements here
import unittest
from collections import defaultdict
"""
Problem : find mamximum seats for new diners by applying social distancing norm by accounting currently sitting diners
Solution Approach:
  seats are one based and list is zero based (ensure during the seat assignment and calculation)
  build a lookup dict that will tell if the seat is occupied or empty
  loop through the N from starting from K till N and increment by K
    check both sides if accupied, if not that seat is available
    may have to deal separately for first seat and last seat
    
pseudo code:
  occupied = defaultdict(bool)
  pupulate the dict
  count
  for i in range(0, N, K):
    # check three condition
    if i != 0 and not occupied(S[i-K]) and 
       i != N-1 and not occupied(S[i+K]) and not occupied(S[i]):
        count += 1
  return count
  
Time Commplexity: O( n/ k) where n is length and k is distancing 
Space Complexity: O(n/k)
"""

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S.sort()
    count = 0
    
    # Before the first occupied seat
    if S[0] - 1 > K:
        count += (S[0] - 1) // (K + 1)
    
    # Between the occupied seats
    for i in range(1, M):
        # Calculating the potential number of additional diners in the gap
        gap = S[i] - S[i - 1] - 1
        if gap > 2 * K:
            count += (gap - K) // (K + 1)
    
    # After the last occupied seat
    if N - S[-1] > K:
        count += (N - S[-1]) // (K + 1)
    
    return count




def getMaxAdditionalDinersCount2(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  if N == 1:
    return 1 if M == 0 else 0
  
  occupied = defaultdict(bool)
  for i in S:
    occupied[i-1] = True
    
  count = 0
  
  for i in range(0, N):
    if not occupied[i]:
      left , right = True, True
      for j in range(1,K+1):
        if i-j >= 0 and occupied[i-j]:
          left = False
        if i+j <= N-1 and occupied[i+j]:
          right = False
      if left and right:
        count +=1
        occupied[i] = True
    
  return count


class TestSolution(unittest.TestCase):
  def test_given_cases(self):
    self.assertEqual(getMaxAdditionalDinersCount(10,1,2,[2,10]), 3)
    self.assertEqual(getMaxAdditionalDinersCount(15,2,3,[11,6,14]), 1)


if __name__ == '__main__':
  unittest.main()