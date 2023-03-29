# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

# A ListNode class is defined, which has two attributes: val (the value of the node) and next (a reference to the next node in the list).

# The mergeTwoLists method is defined, taking two singly-linked lists, list1 and list2, as input.

# A dummy node is created, which serves as a placeholder for the head of the new merged list. The tail variable is initialized to reference this dummy node.

# A while loop runs as long as both list1 and list2 are not empty (i.e., they still have nodes to be processed).

# Inside the loop, the method compares the values of the current nodes in list1 and list2. If the value of the current node in list1 is smaller, the
# tail's next attribute is set to reference this node, and list1 is updated to reference its next node. Otherwise, the tail's next attribute is set to reference
# the current node in list2, and list2 is updated to reference its next node.

# After updating the next attribute of the tail, the tail is updated to reference the newly added node.

# When the loop ends, it means that one of the lists (either list1 or list2) has been completely processed, and the other list still has
# nodes left. In this case, the tail's next attribute is set to reference the remaining nodes of the non-empty list.

# Finally, the method returns the next attribute of the dummy node, which is the head of the new merged list.

# The mergeTwoLists method works by iterating through both input lists, comparing node values, and constructing the new sorted list by linking the nodes
# together in the correct order.