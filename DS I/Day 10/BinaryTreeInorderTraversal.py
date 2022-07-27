# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        x=[]
        for i in self.inorderTraversal(root.left):
            x.append(i)
        x.append(root.val)
        for i in self.inorderTraversal(root.right):
            x.append(i)
        return x
