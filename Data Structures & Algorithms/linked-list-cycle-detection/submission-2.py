# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        if head is None:
            return False
        fast = fast.next
        
        while fast != None:
            if fast.next is None:
                return False
            if fast.val == slow.val:
                return True
            fast = fast.next.next
            slow = slow.next
        
        return False
        