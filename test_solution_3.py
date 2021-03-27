class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def lca(root, n1, n2):
    """

    :param root: The root node
    :param n1: a random node
    :param n2: another node
    :return: the least common ancestor of the given nodes(n1, n2)
    """
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lca = lca(root.left, n1, n2)
    right_lca = lca(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca


if __name__ == '__main__':
    root_node = Node(1)
    root_node.left = Node(2)
    root_node.right = Node(3)
    root_node.left.left = Node(4)
    root_node.left.right = Node(5)
    root_node.left.left.left = Node(8)
    root_node.left.left.right = Node(9)
    root_node.right.left = Node(6)
    root_node.right.right = Node(7)
    print(lca(root_node, 3, 7).key)

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
