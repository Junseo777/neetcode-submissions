# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        subHead = slow.next
        slow.next = None
        
        def reverseList(subHead):
            prev = None
            curr = subHead
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        tail = reverseList(subHead)
        curr = head
        curr2 = tail
        while curr2:
            nxt = curr.next
            curr.next = curr2
            curr2=curr2.next
            curr = curr.next
            curr.next = nxt
            curr = curr.next

        