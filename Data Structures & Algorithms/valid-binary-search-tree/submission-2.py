# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #O(n) time o(h+n)space
        arr = []
        dupchecker = set()
        def dfs(root):
            nonlocal arr
            nonlocal dupchecker
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dupchecker.add(root.val)
            dfs(root.right)
        
        dfs(root)

        if len(arr) > len(dupchecker):
            return False
        if arr == sorted(arr):
            return True
        return False

        