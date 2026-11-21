# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        if head == None or head.next == None:
            return False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        
        return False