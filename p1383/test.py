import unittest
import numpy as np
import numpy.linalg as la
from sol import Solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.sol = Solution()

    def test_basic(self):
        arr = np.array([1, 2, 3, 4])
        probs = np.array([0.1, 0.5, 0.2, 0.2])
        vals = []
        for _ in range(int(10e5)):
            vals.append(self.sol.solve(arr, probs))
            
        hist = np.histogram(np.array(vals), bins=len(arr))[0]
        true_probs = hist / hist.sum()
        print(f'expected probs: {probs}, actual probs: {true_probs}')
        diff = la.norm(probs - true_probs, 2)
        self.assertLessEqual(diff, 10e-4, f'probabilities not the same')
        