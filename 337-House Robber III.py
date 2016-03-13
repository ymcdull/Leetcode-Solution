# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Always iterate a list containing the intermediate result of (rob, not rob)
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))
    
    def dfs(self, root):
        if not root:
            return [0,0]
        lres = self.dfs(root.left)
        rres = self.dfs(root.right)
        res0 = root.val + lres[1] + rres[1]
        res1 = max(lres) + max(rres)
        
        return [res0, res1]
