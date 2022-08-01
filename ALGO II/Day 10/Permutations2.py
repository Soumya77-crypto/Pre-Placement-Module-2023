class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set(tup for tup in itertools.permutations(nums))
        return list(ans)
