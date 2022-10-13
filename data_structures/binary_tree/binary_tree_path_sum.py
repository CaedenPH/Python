"""
Given the root of a binary tree and an integer target, 
find the number of paths where the sum of the values
along the path equals target.


Leetcode reference: https://leetcode.com/problems/path-sum-iii/
"""

from __future__ import annotations


class Node:
    """
    A Node has data variable and pointers to Nodes to its left and right.
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


class BinaryTreePathSum:
    r"""
    The below tree looks like this
          10
         /  \
        5   -3
       / \    \
      3   2    11
     / \   \
    3  -2   1
    

    >>> tree = Node(10)
    >>> tree.left = Node(5)
    >>> tree.right = Node(-3)
    >>> tree.left.left = Node(3)
    >>> tree.left.right = Node(2)
    >>> tree.right.right = Node(11)
    >>> tree.left.left.left = Node(3)
    >>> tree.left.left.right = Node(-2)
    >>> tree.left.right.right = Node(1)

    >>> BinaryTreePathSum(tree).path_sum(8)
    3
    >>> BinaryTreePathSum(tree).path_sum(7)
    1
    >>> tree.right.right = Node(10)
    >>> BinaryTreePathSum(tree).path_sum(8)
    2
    """

    def __init__(self, tree: Node) -> None:
        self.tree = tree

    def depth_first_search(self, node: Node | None) -> int:
        """

        """
        if node is None:
            return 0

        return self.depth_first_search(node)

    def path_sum(self, target: int) -> int:
        """


        """
        return self.depth_first_search(self.tree, target)
    

if __name__ == "__main__":
    import doctest

    doctest.testmod()
