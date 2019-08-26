# Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.

# If the given node has no in-order successor in the tree, return null.

    #       5
    #      / \
    #     3   6
    #   / \
    #   2   4
    #  /
    # 1

    # target = 3, successor = 4

    # 1. Find target - compare root with target
    #     - root > target:
    #         parent #might not be immediate parent
    #     - root < target

    # 2. Find successor
    #     - No root -> None
    #     - No root.right -> parent
    #     - root.right, root.left
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root, p):
        # Find target node
        parent = None
        while root:
            if root.val > p.val:
                parent = root
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                break

        # root is target node or null
        if not root or not (root.right or parent):
            return None

        if not root.right:
            if not parent:
                return None
            # elif parent.val < p.val:
            #     return None
            else:
                return parent

        root = root.right
        while root.left:
            root = root.left

        return root


def printRes(result):
    if result:
        print(result.val)
    else:
        print("None")


def test():
    sol = Solution()

    root = None
    target = None
    result = sol.inorderSuccessor(root, target)
    printRes(result)

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    target = root.left
    result = sol.inorderSuccessor(root, target)
    printRes(result)


test()
