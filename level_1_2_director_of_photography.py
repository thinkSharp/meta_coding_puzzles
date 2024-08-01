# Write any import statements here
import unittest
from collections import defaultdict
"""
Understanding the problem:
Artistic Photo means the distance between Actor with Photographer and Actor with Backdrop must fall between (X, Y) inclusive
Example:
C= APABA 
i= 01234
A = [0,2,4]
P = [1]
B = [3]

Calculated distances (0,1,3)(2,1,3),(4,1,3)
if distances fall between X, Y inclusive count ++

pseudo code
create dictionary of positions
permutate APB , if meet criteria count++

Time complexity O(len(A) * len(B) * len(P)) + O(N) looping to calculate worst cast
Space Complexity O(4)
"""
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  if N <= 1:
    return 0
  
  pos = defaultdict(list)
  for i in range(N):
    pos[C[i]].append(i)
    
  if (X>=0 and Y > 0) and (pos['A'] == 0 or pos['B'] == 0 or pos['P'] == 0):
    return 0
  
  count = 0

  for a in pos['A']:
    for b in pos['B']:
      dis_ab = abs(a-b)
      if dis_ab >= X and dis_ab <= Y:
        for p in pos['P']:
          dis_ap = abs(a-p)
          if dis_ap >= X and dis_ap <= Y:
              
            if p <= a <=b or b <= a <= p:
              count +=1
              print(f'{a} - {b} - {p}')

  return count

class TestSolution(unittest.TestCase):
  def test_given_cases(self):
    self.assertEqual(getArtisticPhotographCount(8,'.PBAAP.B',1,3),3)
    self.assertEqual(getArtisticPhotographCount(5,'APABA',1,2),1)
    self.assertEqual(getArtisticPhotographCount(5,'APABA',2,3),0)

if __name__ == '__main__':
  unittest.main()