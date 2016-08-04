# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        ### Recursive
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root
        if p.val == root.val:
            return p
        if q.val == root.val:
            return q
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
            
        
        ### Iterative
        if p.val > q.val:
            large = p
            small = q
        else:
            large = q
            small = p
        
        if not root:
            return None
        
        while root:
            if root.val >= small.val and root.val <= large.val:
                return root
            elif root.val > large.val:
                root = root.left
            else:
                root = root.right
