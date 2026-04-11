class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen =set()
        count=0
        for i in nums:
            if i in seen:
                count+=1
            else:
                seen.add(i)
        if count==0:
            return False
        else:
            return True        