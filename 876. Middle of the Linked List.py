# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize two pointers, slow and fast, to the head of the linked list
        slow = head
        fast = head

        # while the fast pointer is not at the end of the linked list
        # (i.e., the fast pointer has a next node and the next node also has a next node)
        while fast and fast.next:
            # move the slow pointer one node forward
            slow = slow.next
            # move the fast pointer two nodes forward
            fast = fast.next.next

        # return the node pointed to by the slow pointer, which is the middle node of the linked list
        return slow