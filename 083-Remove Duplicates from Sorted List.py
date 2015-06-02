# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return head
        dict = {}
        guard = ListNode(0)
        guard.next = head
        p = guard
        q = head
        while q:
            if q.val not in dict:
                dict[q.val] = 1
                p = p.next
                q = q.next
            else:
                p.next = q.next
                q = p.next
        return head
