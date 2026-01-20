class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in map:
                return [map[comp], i]
            map[num] = i

a = Solution()
b = a.twoSum([2,7,11,15], 9)
print(b)