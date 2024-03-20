# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binaryTree(start, end):
            if start>end:
                return None
            mid = (start+end)//2
            root = TreeNode(nums[mid])
            root.left = binaryTree(start, mid-1)
            root.right = binaryTree(mid+1, end)
            return root
        return binaryTree(0,len(nums)-1)
        