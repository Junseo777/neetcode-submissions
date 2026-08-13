# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #preorder dfs or bfs
       
        queue = deque()
        stack = []
        if root:
            queue.append(root)
    
        while len(queue) > 0:

            for i in range(len(queue)):
                
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    stack.append(curr.left)
                else:
                    stack.append(None)
                if curr.right:
                    queue.append(curr.right)
                    stack.append(curr.right)
                else:
                    stack.append(None)
               
                curr.left = stack.pop()
                
                curr.right = stack.pop()
               
        return root
            
        