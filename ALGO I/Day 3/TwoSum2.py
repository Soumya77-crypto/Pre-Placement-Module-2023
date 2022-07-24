class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        # Adjust pointer position relative to the number sum
        while left != right:
            if numbers[right] + numbers[left] > target:
                right -= 1
            elif numbers[right] + numbers[left] < target:
                left += 1
            else:
                # sum equals target
                return [left+1,right+1]
        
