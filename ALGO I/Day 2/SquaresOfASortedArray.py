class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
         l=len(nums)
         ans=[]
         for i in range(l):
            ans.append(nums[i]**2)
         ans.sort()
         return ans
