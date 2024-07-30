# Write any import statements here
import unittest
"""
Problem understanding: if given 2 integer A and B find uniform integers between them inclusive
Example: 75, 300 => 77,88,99,111,222 => 5
Example: 1 9 => 1,2,3,4,5,6,7,8,9 => 9
Example: 999999999999 99999999999 => 1 because 99999999999 is inclusive and uniform

Pseudo Code:
calculate start:
   divide by 10 if co
      last uniform number is 10 - 1 = 9
      9 - start = x
   divide by 10 * 10 :
     100 - 1 = 99 - 11 = 88 - 11 = 77 - 11 = 66 exit 
     
   divide by 100 * 10 :
      1000 - 1 = 999 - 111 = 888 -111 = 777 - 111 = 666 - 111 = 
      
      
   middle 100 till 100000 * 10
      + 10
single digit count them all
double digit 11,22,33, 44, 55, so on
same with third and so on

take first 
"""
def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here

  return count


class TestSolution(unittest.TestCase):
  def test_given_cases(self):
    self.assertEqual(getUniformIntegerCountInInterval(1,9), 9)
    self.assertEqual(getUniformIntegerCountInInterval(75, 300), 5)



if __name__ == '__main__':
  unittest.main()



