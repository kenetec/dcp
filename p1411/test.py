import unittest
from sol import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.sol = Solution()

    def test_equality(self):
        s = TreeNode(10, 
                     TreeNode(9, 
                            TreeNode(8, 
                                TreeNode(7),
                                TreeNode(6)
                            ), 
                            TreeNode(5)), 
                     TreeNode(4, 
                            TreeNode(3,
                                TreeNode(2),
                                TreeNode(1),
                            ),
                            TreeNode(0)))
        
        self.assertTrue(self.sol.solve(s, s))

    
    def test_sub_equality(self):
        s = TreeNode(10, 
                     TreeNode(9, 
                            TreeNode(8, 
                                TreeNode(7),
                                TreeNode(6)
                            ), 
                            TreeNode(5)), 
                     TreeNode(4, 
                            TreeNode(3,
                                TreeNode(2),
                                TreeNode(1),
                            ),
                            TreeNode(0)))

        t = TreeNode(3,
                TreeNode(2),
                TreeNode(1),
            )
        
        self.assertTrue(self.sol.solve(t, s))

    
    def test_inequal(self):
        s = TreeNode(10, 
                     TreeNode(9, 
                            TreeNode(8, 
                                TreeNode(7),
                                TreeNode(6)
                            ), 
                            TreeNode(5)), 
                     TreeNode(4, 
                            TreeNode(3,
                                TreeNode(2),
                                TreeNode(1),
                            ),
                            TreeNode(0)))

        t = TreeNode(2,
                TreeNode(1),
                TreeNode(-1),
            )
        
        self.assertFalse(self.sol.solve(t, s))


    def test_same_structure_diff_values(self):
        s = TreeNode(10, 
                     TreeNode(9, 
                            TreeNode(8, 
                                TreeNode(7),
                                TreeNode(6)
                            ), 
                            TreeNode(5)), 
                     TreeNode(4, 
                            TreeNode(3,
                                TreeNode(2),
                                TreeNode(1),
                            ),
                            TreeNode(0)))
        t = TreeNode(101, 
                     TreeNode(91,
                            TreeNode(81, 
                                TreeNode(71),
                                TreeNode(61)
                            ), 
                            TreeNode(51)), 
                     TreeNode(41, 
                            TreeNode(31,
                                TreeNode(21),
                                TreeNode(11),
                            ),
                            TreeNode(1)))
        
        self.assertFalse(self.sol.solve(t, s))


if __name__ == '__main__':
    unittest.main()