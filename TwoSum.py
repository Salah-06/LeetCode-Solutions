class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in map:
                print([map[comp], i])
                return [map[comp], i]
            map[num] = i

a = Solution()
a.twoSum([2,7,11,15], 9)