class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums2=[]
        for i in range(len(nums)):
            if nums[i] not in nums2:
                if nums.count(nums[i])>((len(nums))/3):
                    nums2.append(nums[i])
        return nums2