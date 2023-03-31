# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize prev as None and curr as the head of the list
        prev, curr = None, head

        # Iterate over the list until we reach the end
        while curr:
            # Save the next node in the list
            nxt = curr.next
            # Set the current node's next pointer to the previous node
            curr.next = prev
            # Update prev to be the current node
            prev = curr
            # Update curr to be the next node in the list
            curr = nxt
        # Return the new head of the list, which is the last node we processed
        return prev
