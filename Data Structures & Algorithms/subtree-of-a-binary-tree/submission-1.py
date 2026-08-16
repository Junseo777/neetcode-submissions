# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if not subRoot and root:
            return True
        if root.val == subRoot.val:
            if self.sameTree(root, subRoot):
                return True
        
        if self.isSubtree(root.left, subRoot):
            return True
        return self.isSubtree(root.right,subRoot)

        

    def sameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        if not self.sameTree(p.left, q.left):
            return False
        return self.sameTree(p.right, q.right)


    