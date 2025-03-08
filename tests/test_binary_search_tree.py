import pytest
from src.binary_search_tree import BinarySearchTree, Node

def test_bst_empty_tree_insertion():
    """Test inserting into an empty tree creates root"""
    bst = BinarySearchTree()
    node = bst.insert(5)
    
    assert bst.root is not None
    assert bst.root.key == 5
    assert bst.root.left is None
    assert bst.root.right is None

def test_bst_multiple_insertions():
    """Test multiple insertions maintain BST properties"""
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    
    # Check root
    assert bst.root.key == 5
    
    # Check left subtree
    assert bst.root.left.key == 3
    assert bst.root.left.left.key == 1
    assert bst.root.left.right.key == 4
    
    # Check right subtree
    assert bst.root.right.key == 7
    assert bst.root.right.left.key == 6
    assert bst.root.right.right.key == 8

def test_bst_duplicate_insertions():
    """Test inserting duplicate values"""
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(5)
    
    # Duplicates go to the right
    assert bst.root.key == 5
    assert bst.root.right is not None
    assert bst.root.right.key == 5

def test_bst_none_insertion_raises_error():
    """Test that inserting None raises a TypeError"""
    bst = BinarySearchTree()
    
    with pytest.raises(TypeError, match="Cannot insert None as a key"):
        bst.insert(None)

def test_bst_returns_inserted_node():
    """Test that insert method returns the newly created node"""
    bst = BinarySearchTree()
    node = bst.insert(5)
    
    assert isinstance(node, Node)
    assert node.key == 5

def test_bst_large_number_of_insertions():
    """Test inserting a large number of values"""
    bst = BinarySearchTree()
    values = [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 16, 19]
    
    for val in values:
        bst.insert(val)
    
    # Verify each value is in the tree
    current = bst.root
    assert current.key == 10
    
    # Manually verify some key positions to ensure BST property
    assert current.left.key == 5
    assert current.right.key == 15
    assert current.left.left.key == 3
    assert current.right.left.key == 12