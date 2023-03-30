class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to point to the head of the merged list
        dummy = ListNode()
        # Initialize the tail to the dummy node
        tail = dummy

        # Keep iterating while both lists have elements
        while list1 and list2:
            # If the current node in list1 has a smaller value than the current node in list2
            if list1.val < list2.val:
                # Set the next node after the tail to be the current node in list1
                tail.next = list1
                # Move the pointer in list1 to the next node
                list1 = list1.next
            else:
                # Set the next node after the tail to be the current node in list2
                tail.next = list2
                # Move the pointer in list2 to the next node
                list2 = list2.next
            # Move the tail pointer to the next node
            tail = tail.next

        # If there are remaining nodes in list1, append them to the end of the merged list
        if list1:
            tail.next = list1
        # If there are remaining nodes in list2, append them to the end of the merged list
        elif list2:
            tail.next = list2
        # Return the merged list
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