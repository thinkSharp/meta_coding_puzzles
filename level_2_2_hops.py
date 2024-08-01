import unittest
from typing import List
# Write any import statements here
"""
Problem Understanding: N pads and F frogs and array of F positions. 
We have to find an optimal way of getting all the F to Nth pad which is next to the shore

Example: 

Pseudo Code:
Count 
last_seen_i = 0

loop till N
  pad = [0] * N
  for i in P:
    pad[p[i]] = 1
  
  for i in range(N):
    if pads[i] == 1:
      if last_seen_1 == 0:
        last_seen_1 = i
      for j in range(last_seen_1+1, N):
        if pads[j] == 0:
          pads[i] = 1
          last_seen_i +=1
          count += 1
          break
          
 Time Complexity: (2 * N) => O(N)
 Space complexity: O(N)
"""
def getSecondsRequired_first(N: int, F: int, P: List[int]) -> int:
  # Write your code here
  if F == 1:
    return N - P[0]
  
  count = 0
  last_seen_f = 0
  
  pads = [0] * (N + 1)
  for i in P:
    pads[i] = 1
    
  for i in range(N):
    if pads[i] == 1:
      if last_seen_f == 0:
        last_seen_f = i
      for j in range(last_seen_f +1, N+1):
        if pads[j] == 0:
          if j != N:
            pads[j] = 1
            last_seen_f = j
          pads[i] = 0
          count += 1
          break
        elif pads[j] == 1:
          last_seen_f = j
        if j == N:
          count += 1
          pads[i] = 0
          
  return count

# time complexity: O(FlogF)
def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    if F == 1:
      return N - P[0]
    
    second = 0
    
    P.sort()

    for i in range(F):
      if i + 1 != F:
        hops = P[i+1] - P[i]
        second += hops - 1 if hops != 0 else 0 
    
    second += (N-1) - P[-1]
    second += F
      

    return second

class TestSolution(unittest.TestCase):
  def test_given_cases(self):
    self.assertEqual(getSecondsRequired(3,1,[1]), 2)
    self.assertEqual(getSecondsRequired(6,3,[5,2,4]), 4)
    self.assertEqual(getSecondsRequired(10,3,[1,5,6]), 9)
    self.assertEqual(getSecondsRequired(10,3,[1,5,9]), 9)


if __name__ == '__main__':
  unittest.main()