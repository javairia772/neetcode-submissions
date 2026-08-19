# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        res = ListNode(0)
        res.next = head
        
        fast, slow = res, res
        
        # move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
            
        # move both pointers until fast reaches the last node
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            
        # skip the  target node
        slow.next = slow.next.next
        
        return res.next

        