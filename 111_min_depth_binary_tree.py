class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def _check_depth(node):
            if not node:
            # whenever there's no node, then depth is 0
                return 0
            elif node.left and node.right:
            # whenever there's both a left and right node, you see which child has minimum depth
                return 1+min(_check_depth(node.left),_check_depth(node.right))
            elif node.left or node.right:
            # whenever 1 node is not null, then the other will return 0 and you keep checking if the one-child has more "generations"
                return 1+_check_depth(node.left)+_check_depth(node.right)
            else:
            # whenever there's no leaf nodes, then the current node is a leaf so depth has increased by 1.
                return 1
        return _check_depth(root)