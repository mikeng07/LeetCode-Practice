import unittest
from solution import Solution  
# Import Solution from solution.py
from tree import build_tree   
# Import build_tree from tree.py


class TestDiameterOfBinaryTree(unittest.TestCase):

    def test_diameter_balanced_tree(self):
        # Balanced tree test
        test_tree = build_tree([1, 2, 3, 4, 5, 6, 7])
        sol = Solution()
        self.assertEqual(sol.diameterOfBinaryTree(test_tree), 4, "Balanced tree test failed")

    def test_diameter_left_heavy_tree(self):
        # Left heavy tree test
        test_tree = build_tree([1, 2, None, 3])
        sol = Solution()
        self.assertEqual(sol.diameterOfBinaryTree(test_tree), 2, "Left heavy tree test failed")

    def test_diameter_right_heavy_tree(self):
        # Right heavy tree test
        test_tree = build_tree([1, None, 2, None, None, 3])
        sol = Solution()
        self.assertEqual(sol.diameterOfBinaryTree(test_tree), 2, "Right heavy tree test failed")

    def test_diameter_single_node_tree(self):
        # Single node tree test
        test_tree = build_tree([1])
        sol = Solution()
        self.assertEqual(sol.diameterOfBinaryTree(test_tree), 0, "Single node tree test failed")

    def test_diameter_empty_tree(self):
        # Empty tree test
        test_tree = build_tree([])
        sol = Solution()
        self.assertEqual(sol.diameterOfBinaryTree(test_tree), 0, "Empty tree test failed")

# Additional tests can be added here

if __name__ == "__main__":
    unittest.main()