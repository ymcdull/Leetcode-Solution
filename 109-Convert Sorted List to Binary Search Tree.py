# First transfer the linked list to array, then use recursion to transfer it to binary tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if not head:
            return None
        alist = []
        p = head
        while p:
            alist.append(p.val)
            p = p.next
        return self.transfer(alist)
    
    def transfer(self, alist):
        if len(alist) == 0:
            return None
        m = (len(alist)) / 2
        root = TreeNode(alist[m])
        root.left = self.transfer(alist[:m])
        root.right = self.transfer(alist[m+1:])
        return root
        
