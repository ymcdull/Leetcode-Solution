# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        n = len(preorder)        
        def dfs(pleft, pright, ileft, iright):
            if pleft > pright or ileft > iright:
                return
            value = preorder[pleft]
            root = TreeNode(value)
            if pleft == pright:
                return root

            
            index = inorder.index(value)
            
            root.left = dfs(pleft+1, index-ileft+pleft, ileft, index-1)
            root.right = dfs(pright-iright+index+1, pright, index+1, iright)
            
            return root
                
        
        
        if not preorder or not inorder:
            return None

        return dfs(0,n-1,0,n-1)
