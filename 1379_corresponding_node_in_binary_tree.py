class Solution:
    # there are three cases
    # either original or cloned is None in which case we've went down the wrong path
    # or original == target
    # otherwise original != target
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or not cloned:
            return None
        elif original == target:
            return cloned
        else:
            return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
