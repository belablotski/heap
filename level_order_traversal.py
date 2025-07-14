"""
Problem: Binary Tree Level Order Traversal

Description:
Given the root of a binary tree, return the level order traversal of its nodes' values. This means you should traverse the tree from
left to right, level by level.

Example:

Given the binary tree with root [3,9,20,null,null,15,7]:

1     3
2    / \
3   9  20
4     /  \
5    15   7

The expected level order traversal output is:

1 [
2   [3],
3   [9,20],
4   [15,7]
5 ]
"""

import math
import queue

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode) -> list[list[int]]:
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).
    """
    result = []
    if root:
        nodes = queue.Queue()
        nodes.put((root, 0))
        while not nodes.empty():
            node, level = nodes.get()
            if len(result) == level:
                result.append([node.val])
            else:
                result[level].append(node.val) 
            if node.left:
                nodes.put((node.left, level+1))
            if node.right:
                nodes.put((node.right, level+1))
    return result

def array_to_tree(arr):
    
    def parent_children(parent, l, r):
        if l < len(arr) and arr[l] is not None:
            parent.left = TreeNode(arr[l])
            parent_children(parent.left, 2 * l + 1, 2 * l + 2)
        if r < len(arr) and arr[r] is not None:
            parent.right = TreeNode(arr[r])
            parent_children(parent.right, 2 * r + 1, 2 * r + 2)

    if not arr:
        return None

    depth = math.log2(len(arr)+1)
    if not depth.is_integer():
        raise ValueError("Input array does not represent a complete binary tree")
    
    root = TreeNode(arr[0])
    parent_children(root, 1, 2)

    return root


tree = array_to_tree([3, 9, 20, None, None, 15, 7])
#tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert levelOrder(tree) == [[3], [9, 20], [15, 7]]

tree = array_to_tree([3, 9, 20, 5, None, 15, 7])
assert levelOrder(tree) == [[3], [9, 20], [5, 15, 7]]

tree = array_to_tree([3, 9, 20, 5, 11, 15, 7])
assert levelOrder(tree) == [[3], [9, 20], [5, 11, 15, 7]]

tree = array_to_tree([3, None, 20, None, None, None, 7])
assert levelOrder(tree) == [[3], [20], [7]]

print("All done!")