class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        values = {}

        for value in nums:
            if value not in values:
                values[value] = 1
            else:
                return True
        
        return False

        