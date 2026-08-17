# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        res = ""
        
        def dfs(root):
            nonlocal counter
            nonlocal res
            if not root:
                return False
           
            if dfs(root.left):
                return True
            counter +=1

            if counter == k:
                res = root.val
                return True
            
            return dfs(root.right)
        
        
        dfs(root)
        return res
        #O(n) time complexity
        #O(n) space
        