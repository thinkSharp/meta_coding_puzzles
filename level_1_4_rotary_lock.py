import unittest
from typing import List
# Write any import statements here
"""
Understand the Problem:
each unit rotation take 1 second either direction
there are 1 to N integer
the wheel is initially point to 1
M integer sequence
Minimum number of sequence require to to select all M code integer in order

Example:
N = 10
C = [5,4,9,3,6,5]
4 + 1 + 4 + 3 + 3 + 1

def calculate_second(start, num, N):
  example: 
  1, 4, 10 => 4-1 = 3 or 10 - 4 + 4 - 1 + 1
  4, 9 10  => 9-4 = 5 or (10 - 9) + 1 + (4 - 1) = 5
  5, 4, 10 => 4 - 5 = -1 or (10 - 4) + 1 + (4 -1) = 9
  9, 1, 10 => 1 - 9 = -8 or (10 - 9) + 1 = 2
main method
  loop C:
    count +=call calculate_second()
    
  return count
  

Time complexity = O(n) => n is the len of C
space complexity = O (1)
"""

# did get help for this method
# did not know that modulo operation in python return positive value for a negative numer
# example: -3 % 10 = 7
def calculate_second(start, dest, N):
  
  forward = (start - dest) % N
  backward = (dest - start) % N

  return min(forward, backward)


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  seconds = 0
  current = 1
  for code in C:
    seconds += calculate_second(current, code, N)
    print(seconds)
    current = code
    
  return seconds


class TestSolution(unittest.TestCase):
  def test_calculate_second_cases(self):
    self.assertEqual(calculate_second(1, 4, 10), 3)
    self.assertEqual(calculate_second(9, 2, 10), 3)
    self.assertEqual(calculate_second(2, 9, 10), 3)
  

  def test_given_cases(self):
    self.assertEqual(getMinCodeEntryTime(3,3,[1,2,3]), 2)
    self.assertEqual(getMinCodeEntryTime(10,4,[9,4,4,8]), 11)
    

  def test_complext_cases(self):
    self.assertEqual(getMinCodeEntryTime(10000000, 3, [500000, 5000000, 9500000]), 9499999)
    self.assertEqual(getMinCodeEntryTime(1000000, 5, [1, 3, 5, 7, 9]), 8)
    self.assertEqual(getMinCodeEntryTime(50000000, 4, [1, 25000000, 50000000, 1]), 50000000)
    self.assertEqual(getMinCodeEntryTime(10000000,6,[999999, 1000001, 1000002, 1000005, 1000010, 1000020]),  1000019)
    self.assertEqual(getMinCodeEntryTime(20000000, 7, [1, 5000000, 10000000, 15000000, 20000000, 10000000, 1]), 39999998)
    #self.assertEqual(getMinCodeEntryTime(50000000,8,[49999999, 1, 2, 50, 1000, 49999000, 50000000, 1]),  50000004 )
    

if __name__ == '__main__':
  unittest.main()
