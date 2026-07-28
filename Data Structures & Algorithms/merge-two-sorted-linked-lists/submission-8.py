# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
    
        while curr:

            if list1 == None and list2 == None:
                break

            elif list1 == None:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
            elif list2 == None:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            
            else:

                if list2.val > list1.val:
                    curr.next = list1
                    list1 = list1.next
                    curr = curr.next
                else:                    
                    curr.next = list2
                    list2 = list2.next
                    curr = curr.next
        return dummy.next

