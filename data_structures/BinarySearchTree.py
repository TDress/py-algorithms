# "from scratch" implementation of binary search tree with rebalancing.

from lib import assertion

class BinarySearchTreeNode:
    """Class representing a single binary tree node."""
    def __init__(self, key, left=None, right=None, parent=None):
        self._key = key
        self._left = left
        self._right = right
        self._parent = parent


def tree_search(node, key):
    """Search the tree for node with key `key`.
    
    If a node with matching key is found, return the node.
    If not found return the last visited node on the search path.
    
    :param BinarySearchTreeNode node: The at which to begin search
    :param int key: The key to search for
    :return BinarySearchTreeNode: The last node on the search path
    """
    if node is None:
        raise ValueError('Argument `node` must be a node object')

    if key < node._key and node._left:
        return tree_search(node._left, key)
    elif key > node._key and node._right:
        return tree_search(node._right, key)

    return node

def node_before(node):
    """Find the node immediately before `node` (in ordering) and return it
    
    :param BinarySearchTreeNode node: The node that comes after the target
    :return BinarySearchTreeNode: The node that comes before `node` or `node`
        if it has no left subtree.
    """
    if not node._left:
        return node

    return tree_search(node._left, node._key)


def insert_node(root, key):
    """Insert node into tree rooted at `root`, without rebalancing.

    If a node with key `key` already exists, abort insertion and 
    return the existing node.
    
    :param BinarySearchTreeNode root: The root of the tree.
    :param int key: The key of the new node to insert.
    :return BinarySearchTreeNode: The new node or the existing node
        with key `key` if found.
    """
    if root is None:
        raise ValueError('Argument `root` must be a node object')
    
    node = tree_search(root, key)
    if node._key != key:
        new_node = BinarySearchTreeNode(key, parent=node)
        if key > node._key:
            node._right = new_node
        else:
            node._left = new_node

    return new_node or node

def remove_node_with_less_children(node):
    """Remove node `node` from tree.

    Precondition: the node has no more than 1 child, so
    we can simply link its child to its parent or simply unlink it
    if it has 0 children.
    
    :param BinarySearchTreeNode node: The node to remove.
    """
    if node._right is not None and node._left is not None:
        raise ValueError('argument violates precondition: no more than 1 child')
    child = node._right or node._left
    # Link the child to its new parent
    try:
        child._parent = node._parent
    except:
        pass

    # Link the parent to its new child
    if node._parent and node._parent._left is node:
        node._parent._left = child
    elif node._parent:
        node._parent._right = child

    node = None

def delete_node(root, key):
    """Delete node with key `key` from tree with root node `root`
    
    The key of the deleted node is returned.  If the node with key
    `key` is not found an exception a ValueError is raised.

    :param BinarySearchTreeNode root: The root of the tree
    :param int key: The key of the node to be deleted
    :return None: 
    :raises ValueError: if the key is not found in the tree    
    """
    if root is None:
        raise ValueError('Argument `root` must be a node object')

    node = tree_search(root, key)
    if node._key != key:
        raise ValueError('Argument `key` not found')
    
    if node._right is not None and node._left is not None:
        # overwrite node with key of that comes immediately before,
        # and delete the node that comes immediately before.
        before = node_before(node)
        node._key = before._key
        remove_node_with_less_children(before)
    else:
        remove_node_with_less_children(node)


def main():
    root = BinarySearchTreeNode(10)

    # test inserting nodes
    assertion.equals(5, insert_node(root, 5)._key)
    assertion.equals(False, root._left is None)
    assertion.equals(5, root._left._key)

    insert_node(root, 3)
    insert_node(root, 4)
    assertion.equals(4, root._left._left._right._key)

    insert_node(root, 15)
    insert_node(root, 18)
    insert_node(root, 11)

    assertion.equals(18, root._right._right._key)
    assertion.equals(11, root._right._left._key)

    # Test searching the binary search tree.
    assertion.equals(3, tree_search(root, 2)._key)
    assertion.equals(10, tree_search(root, 10)._key)
    assertion.equals(11, tree_search(root, 11)._key)
    assertion.equals(18, tree_search(root, 20)._key)

    # Test deletion of nodes
    insert_node(root, 1)
    insert_node(root, 2)
    insert_node(root, 16)
    insert_node(root, 20)
    delete_node(root, 20)
    assertion.equals(18, tree_search(root, 20)._key)
    
    delete_node(root, 15)
    assertion.equals(11, root._right._key)
    assertion.equals(None, root._right._left)
    assertion.equals(5, root._left._key)
    assertion.equals(None, root._left._right)
    assertion.equals(3, root._left._left._key)
    assertion.equals(5, node_before(root)._key)

    delete_node(root, 10)
    assertion.equals(5, root._key)
    assertion.equals(11, root._right._key)
    assertion.equals(3, root._left._key)
    assertion.equals(4, node_before(root)._key)
    

if __name__ == '__main__':
    main()

    

