class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i,j])

nums = [12,22,7,34,55]
target = 19

result = Solution()
print(result.twoSum(nums,target))