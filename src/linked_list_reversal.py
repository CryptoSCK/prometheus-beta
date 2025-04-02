class ListNode:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        val (Any): The value stored in the node.
        next (ListNode, optional): Reference to the next node in the list. Defaults to None.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverses a singly linked list and returns the new head.
    
    Args:
        head (ListNode): The head of the input linked list.
    
    Returns:
        ListNode: The head of the reversed linked list.
    
    Time Complexity: O(n), where n is the number of nodes
    Space Complexity: O(1)
    
    Examples:
        >>> node3 = ListNode(3)
        >>> node2 = ListNode(2, node3)
        >>> node1 = ListNode(1, node2)
        >>> reversed_head = reverse_linked_list(node1)
        >>> # reversed_head will now point to a list: 3 -> 2 -> 1
    """
    # Handle empty list or single node list
    if not head or not head.next:
        return head
    
    # Three-pointer technique for in-place reversal
    prev = None
    current = head
    
    while current:
        # Store the next node before modifying links
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # The prev pointer becomes the new head
    return prev