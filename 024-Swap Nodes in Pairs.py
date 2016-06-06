# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        
        while p.next and p.next.next:
            tmp = p.next
            p.next = p.next.next
            tmp.next = p.next.next
            p.next.next = tmp
            
            p = p.next.next
            
        return dummy.next
