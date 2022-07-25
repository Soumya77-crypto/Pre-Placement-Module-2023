class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
            
        for char in t:
            if char not in counter:
                return False
            else:
                counter[char] -= 1
        
        for key, value in counter.items():
            if value != 0:
                return False     
