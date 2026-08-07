# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        rP = prev

        for i in range(n-2):
            rP = rP.next
        
        if n != 1:
            rP.next = rP.next.next
        else:
            prev = prev.next

        prev2 = None
        curr2 = prev
        while curr2:
            nxt2 = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = nxt2
        
        return prev2