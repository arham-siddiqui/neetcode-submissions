# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        first = list1
        second = list2

        newList = ListNode(0, None)
        curr = newList

        while first != None and second != None:
            if first.val < second.val:
                curr.next = ListNode(first.val, None)
                curr = curr.next
                first = first.next
            else:
                curr.next = ListNode(second.val, None)
                curr = curr.next
                second = second.next
        
        while first != None:
            curr.next = ListNode(first.val, None)
            first = first.next
            curr = curr.next
        while second != None:
            curr.next = ListNode(second.val, None)
            second = second.next
            curr = curr.next
        
        return newList.next
