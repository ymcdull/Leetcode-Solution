# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if not head or not head.next or not head.next.next:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        dummy = ListNode(0)
        dummy.next = head2
        p = head2.next
        head2.next = None
        
        while p:
            tmp = p
            p = p.next
            tmp.next = dummy.next
            dummy.next = tmp
        head2 = dummy.next

        p = head1
        q = head2
        while q:
            tmp = p.next
            p.next = q
            p = tmp
            tmp = q.next
            q.next = p
            q = tmp
