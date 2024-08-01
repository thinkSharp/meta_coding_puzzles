import unittest
# Write any import statements here
from collections import defaultdict
"""
Problem Understanding: Actor must be between Photographer and backdrop. the distance between them must be inclusive of X, Y.
Two photographs are considered different if they involve a different photographa, actor and backdrop. 

Example: APABA 3 A and one P and one B => 1 PAB X = 1 Y = 2 calculate the distance between PA and BA must be between them
APABA X = 2 and Y = 3 so PAB does not fall in the range 0
.PBAAP.B 1, 3 => .P.A...B, ..BA.P, .P..A..B, ..B.AP.. X = 1, 3

Pseudo Code:
  defaultDictionary of P, A, B and their indexes
  loop A indexes:
    loop P indexes
      calcuale the distances, if matches
        loop B indexes:
          calculate the distances if matches
            c++
            visited (p and B)
            
Time Complexity : O(len(index of A) * len(index of B) * len(index of P)) + O(n) 
Space Complexity : O(4)

"""
def getArtisticPhotographCount_n2(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
    count = 0
    indexes = defaultdict(list)
  
    # Store positions of 'P', 'A', and 'B'
    for i in range(N):
        indexes[C[i]].append(i)
    
    photographers = indexes['P']
    backdrops = indexes['B']
    
    # Sliding window pointers for 'P' and 'B'
    p_index = 0
    b_index = 0
    
    # Iterate through each actor
    for a in indexes['A']:
        p_count_left = sum(1 for p in photographers if p < a and X <= abs(a-p) <= Y)
        b_count_right = sum(1 for b in backdrops if b > a and X<=abs(a-b) <= Y)

        p_count_right = sum(1 for p in photographers if p > a and X <= abs(a-p) <= Y)
        b_count_left = sum(1 for b in backdrops if b < a and X<=abs(a-b) <= Y)

        # Count valid photographs for this actor
        count += (p_count_left * b_count_right) + (p_count_right * b_count_left)

    return count

def count_artistic_photographs(N, C, X, Y):
    p_prefix = [0] * (N )
    b_prefix = [0] * (N)

    p_prefix[0] = (1 if C[0] == 'P' else 0)
    b_prefix[0] = (1 if C[0] == 'B' else 0)
    # Compute prefix sums for 'P' and 'B'
    for i in range(1, N):
        p_prefix[i] = p_prefix[i-1] + (1 if C[i] == 'P' else 0)
        b_prefix[i] = b_prefix[i-1] + (1 if C[i] == 'B' else 0)

    count = 0

    # Iterate through each position for 'A'
    for i in range(N):
        if C[i] == 'A':
            left_start = max(i - (Y +1) , 0)
            left_end = max(i - X,0)
            py_count_left = p_prefix[left_end] - p_prefix[left_start]
            by_count_left = b_prefix[left_end] - b_prefix[left_start]

            right_start = max(i, min(i+(X-1), N-1))
            right_end = min(i + Y, N-1)
            py_count_right = p_prefix[right_end] - p_prefix[right_start]
            by_count_right = b_prefix[right_end] - b_prefix[right_start]

            count += py_count_left * by_count_right
            count += by_count_left * py_count_right

                
    return count


class TestSolution(unittest.TestCase):
  """
  def test_O_N_implementation_cases(self):
    self.assertEqual(count_artistic_photographs(8,'.PBAAP.B',1,3),3)
    self.assertEqual(count_artistic_photographs(5,'APABA',1,2),1)
    self.assertEqual(count_artistic_photographs(5,'APABA',2,3),0)

"""
  def test_given_cases(self):
    self.assertEqual(count_artistic_photographs(8,'.PBPABPP',1,3),4)
    self.assertEqual(count_artistic_photographs(8,'.PBAAP.B',1,3),3)
    self.assertEqual(count_artistic_photographs(5,'APABA',1,2),1)
    self.assertEqual(count_artistic_photographs(5,'APABA',2,3),0)



if __name__ == '__main__':
  unittest.main()