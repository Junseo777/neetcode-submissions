# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None

        elif list1 == None:
            curr = list2
            head = curr
            list2 = list2.next
        
        elif list2 == None:
            curr = list1
            head = curr
            list1 = list1.next
        else:

            if list1.val > list2.val:
                curr = list2
                head = curr
                list2 = list2.next
           
            else:
                curr = list1
                head = curr
                list1 = list1.next
           
    
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
        return head

