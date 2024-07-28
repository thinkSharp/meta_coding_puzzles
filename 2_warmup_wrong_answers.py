# Write any import statements here
import unittest

"""
Problem: Get the wrong Answers
Solution Approach: since  potential answers are A, B, Creating a dictionary for a look up to do the job. 
That would be easily extendable as well
pseudo code:
dict = {'A': 'B', 'B': 'A'}
result =[]
loop the C:

return ''.join(result)

Time Complexity: O(n) n is the length of arr
Space Complexity: O(n) + O(A) A is the answer for dictionary
"""
def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  wrong_answer = {'A': 'B', 'B':'A'}
  result = []
  for i in range(N):
    result.append(wrong_answer[C[i]])
  
  return ''.join(result)



class TestCases(unittest.TestCase):
  def test_given_cases(self):
    self.assertEqual(getWrongAnswers(3, 'ABA'),'BAB')
    self.assertEqual(getWrongAnswers(5, 'BBBBB'),'AAAAA')


if __name__ == '__main__':
  unittest.main()