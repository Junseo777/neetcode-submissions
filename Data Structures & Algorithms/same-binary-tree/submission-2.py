# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        sp = []
        sq = []

        def dfs(root,storage):
            if not root:
                storage.append(None)
                return 

            storage.append(root.val)
            dfs(root.left,storage)
            dfs(root.right,storage)

        dfs(p,sp)
        dfs(q,sq)
        
        return (sp==sq)

        
    

