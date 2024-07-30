# Write any import statements here
import unittest
"""
Problem understanding: if given 2 integer A and B find uniform integers between them inclusive
Example: 75, 300 => 77,88,99,111,222 => 5
Example: 1 9 => 1,2,3,4,5,6,7,8,9 => 9
Example: 999999999999 99999999999 => 1 because 99999999999 is inclusive and uniform

Pseudo Code:
    loop through the len of B:
        loop through 1 to 9:
            build uniform digit
            compare with A and B
                Count++
"""
def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here
    count = 0
    for digits in range(1, len(str(B))+1):
       for digit in range(1,10):
          uniform_num = int(str(digit) * digits)
          if A <= uniform_num <= B:
             count +=1
    return count



class TestSolution(unittest.TestCase):
  def test_given_cases(self):
    self.assertEqual(getUniformIntegerCountInInterval(1,9), 9)
    self.assertEqual(getUniformIntegerCountInInterval(75, 300), 5)



if __name__ == '__main__':
  unittest.main()



