# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Check if the root is None, if yes, return an empty list (base case)
        if not root:
            return []

        # Initialize an empty list named 'result' to store the preorder traversal
        result = []

        # Initialize a stack and push the root node onto it
        stack = [root]

        # Start a while loop until the stack is not empty
        while stack:
            # Pop the top node from the stack and assign it to a variable 'node'
            node = stack.pop()

            # Append the value of the 'node' to the 'result' list
            result.append(node.val)

            # Check if the 'node' has children
            if node.children:
                # Iterate through the children of the 'node' in reversed order
                for child in reversed(node.children):
                    # Push each child onto the stack
                    stack.append(child)

        # End of the while loop

        # Return the 'result' list containing the preorder traversal of the n-ary tree
        return result
