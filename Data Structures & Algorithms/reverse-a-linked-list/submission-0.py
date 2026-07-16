# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        if curr == None:
            return None
        newList = ListNode(curr.val, None)
        curr = curr.next

        while curr != None:
            print(curr.val)
            newList = ListNode(curr.val, newList)
            curr = curr.next
        
        return newList
