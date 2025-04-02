import pytest
from src.linked_list_reversal import ListNode, reverse_linked_list

def list_to_array(head):
    """
    Convert a linked list to an array for easy comparison.
    
    Args:
        head (ListNode): Head of the linked list.
    
    Returns:
        list: Values in the linked list.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def array_to_list(arr):
    """
    Convert an array to a linked list.
    
    Args:
        arr (list): Input array of values.
    
    Returns:
        ListNode: Head of the created linked list.
    """
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def test_reverse_empty_list():
    """Test reversing an empty list."""
    assert reverse_linked_list(None) is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node."""
    single_node = ListNode(1)
    reversed_list = reverse_linked_list(single_node)
    assert list_to_array(reversed_list) == [1]

def test_reverse_multiple_node_list():
    """Test reversing a list with multiple nodes."""
    # Original list: 1 -> 2 -> 3 -> 4 -> 5
    input_list = array_to_list([1, 2, 3, 4, 5])
    
    # Expected reversed list: 5 -> 4 -> 3 -> 2 -> 1
    reversed_list = reverse_linked_list(input_list)
    assert list_to_array(reversed_list) == [5, 4, 3, 2, 1]

def test_reverse_two_node_list():
    """Test reversing a list with two nodes."""
    # Original list: 1 -> 2
    input_list = array_to_list([1, 2])
    
    # Expected reversed list: 2 -> 1
    reversed_list = reverse_linked_list(input_list)
    assert list_to_array(reversed_list) == [2, 1]

def test_list_reversal_preserves_node_structure():
    """
    Ensure that reversing the list properly maintains 
    the links between nodes.
    """
    # Original list: 1 -> 2 -> 3
    input_list = array_to_list([1, 2, 3])
    
    reversed_list = reverse_linked_list(input_list)
    current = reversed_list
    
    # Verify node values in order
    assert list_to_array(reversed_list) == [3, 2, 1]
    
    # Verify links are correct
    while current and current.next:
        assert isinstance(current, ListNode)
        assert isinstance(current.next, ListNode)
        current = current.next