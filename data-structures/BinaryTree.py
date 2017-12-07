import Tree

class BinaryTree(Tree):
    """Abstract Base Class for a binary tree structure"""
    def left(self, p):
        """Return a postition representing p's left child"""
        raise NotImplementedError('Must be implemented by a subclass')

    def right(self, p):
        """Return a position representing p's right child"""
        raise NotImplementedError('Must be implemented by a subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


