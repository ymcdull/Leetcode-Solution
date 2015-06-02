# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 对于递归思路，pre-, in- and post- order traversal如出一辙
# 对于循环思路，后续遍历(postorder) 要比前序和中序稍微复杂，入栈时需要先right，后left
# 需要存储上一个出栈的元素prev, 如果该prev是当前root的子节点，表示该root节点的子节点都已遍历，则输出该root

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        
        ### recursive
        
        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        
        ### iterative:
        
        if not root:
            return []
        res = []
        stack = []
        prev = None
        if root:
            stack.append(root)
            while stack:
                root = stack[-1]
                if (not root.left and not root.right) or (prev and (prev == root.left or prev == root.right)):
                    res.append(root.val)
                    prev = root
                    stack.pop()
                else:
                    if root.right:
                        stack.append(root.right)
                    if root.left:
                        stack.append(root.left)
                    
        return res
                
                
                
                
                
        
        
        
