from lib import assertion

class TrieNode:
    # terminating label identifier to indicate leaf at parent node
    TERMINATE = '$'

    def __init__(self, label, is_root=False):
        # hash map of children for fast lookups.  
        # this is what allows us to find a word in O(m) where m is length
        self.children = {}
        self.label = label
        self._is_root = is_root

    def is_root(self):
        return self._is_root


def construct_trie(words):
    """Return root TrieNode of trie containing all words in `words`"""

    root = TrieNode("", True)
    walk = root

    for word in words:
        for c in word:
            if c in walk.children:
                walk = walk.children[c]
            else:
                next = TrieNode(c)
                walk.children[c] = next
                walk = next

        # create marker for terminating word
        term = TrieNode(TrieNode.TERMINATE)
        walk.children[term.label] = term
        walk = root

    return root


def trie_prefix(prefix, root):
    """look for `prefix` in the trie rooted at `root`
    
    :return:    The TrieNode with label equal to the last character in the prefix,
                or False if prefix is not found"""

    if not isinstance(root, TrieNode):
        raise TypeError("Argument `root` is not a TrieNode object")

    walk = root

    for c in prefix:
        if c in walk.children:
            walk = walk.children[c]
        else:
            return False

    return walk


def word_lookup(word, root):
    """Lookup a word in the trie rooted at `root`.

    :return: The terminating node for the word if found, or False"""

    if not isinstance(root, TrieNode):
        raise TypeError("Argument `root` is not a TrieNode object")

    walk = root

    for c in word:
        if c in walk.children:
            walk = walk.children[c]
        else:
            return False

    try:
        return walk.children[TrieNode.TERMINATE]
    except KeyError:
        return False
    


def main():
    trie_root = construct_trie(['are', 'rail', 'ale', 'rain', 'raze', 'raz'])
    # Test prefix lookups
    node = trie_prefix('a', trie_root)
    node2 = trie_prefix('ra', trie_root)
    node3 = trie_prefix('are', trie_root)
    node4 = trie_prefix('z', trie_root)

    assertion.equals(2, len(node.children))
    assertion.equals(True, 'l' in node.children)

    assertion.equals(2, len(node2.children))
    assertion.equals(True, 'z' in node2.children)

    assertion.equals(1, len(node3.children))
    assertion.equals(True, TrieNode.TERMINATE in node3.children)

    assertion.equals(False, node4)

    # test word lookups
    assertion.equals(False, word_lookup('asdfasdf', trie_root))
    assertion.equals(False, word_lookup('qle', trie_root))

    node = word_lookup('are', trie_root)
    node2 = word_lookup('raz', trie_root)
    node3 = word_lookup('raze', trie_root)
    node4 = word_lookup('rail', trie_root)

    assertion.equals(TrieNode.TERMINATE, node.label)
    assertion.equals(TrieNode.TERMINATE, node2.label)
    assertion.equals(TrieNode.TERMINATE, node3.label)
    assertion.equals(TrieNode.TERMINATE, node4.label)
    assertion.equals(0, len(node.children) + len(node2.children) +
                     len(node3.children) + len(node4.children))
    

if __name__ == '__main__':
    main()
