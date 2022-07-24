class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x=set(nums)
        y=len(x)
        if(len(nums)==y):
            return False
        else:
            return True
        
