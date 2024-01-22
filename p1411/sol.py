# Given two non-empty binary trees s and t, 
# check whether tree t has exactly the same structure and 
# node values with a subtree of s. A subtree of s is a tree 
# consists of a node in s and all of this node's descendants. 
# The tree s could also be considered as a subtree of itself.

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.left = left 
        self.right = right 
        self.value = value 

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_empty(self):
        return self.is_leaf() and self.value is None
    

class Solution:
    def __init__(self):
        pass
    
    def solve(self, s: TreeNode, t: TreeNode):
        '''
        traverse s and t in the same order, if there are any discrepancies, report as false 
        '''
        if s is None or t is None:
            raise RuntimeError('Trees should be non-null')
        
        if s.is_empty() or t.is_empty():
            raise RuntimeError('Trees should be non-empty') 

        return self.is_subtree(s, t)
        
    
    def is_subtree(self, s: TreeNode, t: TreeNode): 
        if (s is None and t is not None) or \
            (s is not None and t is None):
            return False

        if (s.is_leaf() and not t.is_leaf()) or (not s.is_leaf() and t.is_leaf()):
            return False
        
        if s.is_leaf() and t.is_leaf():
            return s.value == t.value

        # two possibilities: s and t are corresponding or t corresponds to a child of s (or vice-versa)
        return (s.value == t.value and self.is_subtree(s.left, t.left) and self.is_subtree(s.right, t.right)) or \
            (self.is_subtree(s.left, t) or self.is_subtree(s.right, t)) or \
                (self.is_subtree(t.left, s) or self.is_subtree(t.right, s))