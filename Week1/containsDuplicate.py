class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for _ in nums:
            try:
                if d[_] == 1:
                    return True
            except Exception as e:
                d[_] = 1
        return False