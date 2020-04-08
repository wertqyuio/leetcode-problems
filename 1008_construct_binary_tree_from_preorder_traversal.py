# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
	# iterative solution with a stack
	# keep adding to stack the current node and the relevant ancestor node
	# the ancestor node is to determine how many pops are required when
	# appending right
        start = TreeNode(preorder[0])
        tree = [[start,None]]
        idx = 1
        while idx < len(preorder):
            current = TreeNode(preorder[idx])
            previous = tree[-1]
            if previous[0].val > current.val:
                previous[0].left = current
                tree.append([current, previous[0]])
            else:
                while previous[1] and previous[1].val < current.val:
                    tree.pop()
                    previous = tree[-1]
                previous[0].right = current
                tree.append([current,previous[1]])
            idx += 1
        return start
