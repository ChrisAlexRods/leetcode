# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        # initialize a set to keep track of visited nodes
        lookup = set()

        # iterate through the linked list using the current pointer
        while cur:
            # if the current node has already been visited, then it is the start of a cycle
            if cur in lookup:
                # return the current node
                return cur

            # add the current node to the set of visited nodes
            lookup.add(cur)
            # move the current pointer to the next node
            cur = cur.next

        # if no cycle is found, return None
        return None
