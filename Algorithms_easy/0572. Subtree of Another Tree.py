"""
572. Subtree of Another Tree
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(s,t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            return s.val == t.val and isSame(s.left,t.left) and isSame(s.right,t.right)
        
        def traverse(s,t):
            if not s and not t:
                return True
            elif not s and t:
                return False
            elif s and not t:
                return False
            else:
                if s.val != t.val:
                    return traverse(s.left,t) or traverse(s.right,t)
                else:
                    if traverse(s.left,t) or traverse(s.right,t):
                        return True
                    else:
                        return isSame(s,t)
        
        return traverse(s,t)        
