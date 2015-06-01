# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        p = l1
        q = l2
        head = ListNode((p.val+q.val)%10)
        addition = (p.val+q.val)/10
        t = head
        p = p.next
        q = q.next
        while p and q:
            temp = ListNode((p.val+q.val+addition)%10)
            t.next = temp
            t = t.next
            addition = (p.val+q.val+addition)/10
            p = p.next
            q = q.next
        if not p:
            while q:
                temp = ListNode((q.val+addition)%10)
                addition = (q.val+addition)/10
                t.next = temp
                t = t.next
                q = q.next
        elif not q:
            while p:
                temp = ListNode((p.val+addition)%10)
                addition = (p.val+addition)/10
                t.next = temp
                t = t.next
                p = p.next
        if addition > 0:
            t.next = ListNode(addition)
            
        return head
