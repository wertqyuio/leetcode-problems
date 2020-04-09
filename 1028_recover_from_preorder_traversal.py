 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # use a stack where you push a list containing the node and depth
        S_stack = []
        
        def _push(val, depth):
        # push new nodes
            current = TreeNode(val)
            if not S_stack:
                S_stack.append([current, depth])
            elif depth > S_stack[-1][1]:
                # add current element to left of previous node
                S_stack[-1][0].left = current
                S_stack.append([current,depth])
            else:
                while S_stack[-1][1] >= depth:
                # pop stack until appropriate depth reached
                    S_stack.pop()
                S_stack[-1][0].right = current
                S_stack.append([current,depth])
        
        def _traverse_S(word):
        # convert the string into values to insert into binary tree
            idx = 0
            
            while idx < len(word):
                current = ""
                depth = 0
                while idx < len(word) and word[idx] == "-":
                    depth += 1
                    idx += 1
                while idx < len(word) and word[idx] != "-":
                    current += word[idx]
                    idx += 1
                
                _push(int(current), depth)
        
        _traverse_S(S)
        
        return S_stack[0][0]
