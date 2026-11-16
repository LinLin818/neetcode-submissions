# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        temp = head
        while temp is not None:
            length += 1
            temp = temp.next

        front_end = head
        for _ in range((length - 1) // 2):
            front_end = front_end.next

        stack = []
        curr = front_end.next
        while curr is not None:          # fix 1: while, not for
            stack.append(curr)           # fix 2: push curr, not i
            curr = curr.next
        front_end.next = None

        curr = head
        while stack:
            next_node = curr.next
            backward = stack.pop()
            curr.next = backward
            backward.next = next_node
            curr = next_node             # fix 3: next_node, not next