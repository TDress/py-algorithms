from lib import assertion
from data_structures.HeapPriorityQueue import HeapPriorityQueue
from data_structures.LinkedBinaryTree import LinkedBinaryTree

# Value to use for internal nodes of the huffman tree (in place of a character).
INTERNAL = 'INTERNAL'

def frequencies(S):
    """Helper function for creating a frequency dict of characters in a string"""
    answer = {}
    for c in S:
        if c in answer:
            answer[c] += 1
        else:
            answer[c] = 1
    return answer

def dfs_huffman(T, p, chars, code = ''):
    """Post-order style traversal of tree T, starting at position p.

    The "visit" action for each node sets the value of the chars dict
    for that character to its huffman code.
    We build up the huffman code as we recurse by adding a "0" if we 
    are recursing left, or a "1" if recursing right.  
    
    :param T: A binary tree where each leaf stores a (frequency, character) tuple
    :param p: Position in the binary tree (node)
    :param chars: Character dict  that we will use to store the huffman codes.
    :param code: The code bit string at the current node position
    """
    if T.left(p):
        dfs_huffman(T, T.left(p), chars, code=code+'0')
    if T.right(p):
        dfs_huffman(T, T.right(p), chars, code=code+'1')

    # Add the code if we are not at an internal node (if we have a character at p)
    elem = p.element()
    if elem[1] != INTERNAL:
        chars[elem[1]] = code

def huffman_code(S):
    """Get the huffman encoding (bit string) for string S.

    4 Steps:
        1. Create a dict of characters in S mapped to their frequencies.  Create
            a binary tree for each character with a single node containing the 
            frequency and character and add each tree to a priority queue.
        2. dequeue from the priority queue 2 trees at a time and merge them 
            by creating a new root containing a frequency equal to the sum of the 
            two tree root's frequencies, and attach the first dequeued (first min 
            removed) tree as the left subtree and the other as the right.
        3. Now that you have just one tree, traverse it and build up the huffman
            codes as you descend down each path.  overwrite the dict of char
            frequencies with the codes for the chars.
        4. Iterate over the original string and return the codes in order, 
            concatenated into one bit string!
    """
    chars = frequencies(S)
    initial_trees = []
    for c, freq in chars.items():
        t = LinkedBinaryTree()
        t._add_root((freq, c))
        # The priority queue will use frequencies as keys and trees as values
        initial_trees.append((freq, t))

    p_queue = HeapPriorityQueue(initial_trees)
    while len(p_queue) > 1:
        new_left = p_queue.remove_min()
        new_right = p_queue.remove_min()
        total_freq = new_left[0] + new_right[0]
        t = LinkedBinaryTree()
        t._add_root((total_freq, INTERNAL))
        t._attach(t.root(), new_left[1], new_right[1])
        p_queue.add_item(total_freq, t)

    huff_tree = p_queue.remove_min()[1]
    # traverse the tree and overwrite chars dict values with bit codes.
    dfs_huffman(huff_tree, huff_tree.root(), chars)
    return ''.join((chars[c] for c in S))


def main():
    testS1 = 'ABACA'
    testS2 = 'a fast runner need never be afraid of the dark'

    assertion.equals({'A': 3, 'B': 1, 'C': 1}, frequencies(testS1))
    assertion.equals({'a': 5, 'b': 1, 'd': 3, 'e': 7, 'f': 3, 'h': 1,
                      'i': 1, 'k': 1, 'n': 4, 'o': 1, 'r': 5, 's': 1, 
                      't': 2, 'u': 1, 'v': 1, ' ': 9}, frequencies(testS2))

    assertion.equals('1001011', huffman_code(testS1))
    # Can't test for an exact encoding of S2 since there are multiple 
    # possible huffman trees based on the order of items dequeued from
    # the priority queue that have equal keys.
if __name__ == '__main__':
    main()


