# class Solution:
#     def twoSum(self,nums,target):
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return ([i,j])
# nums = [12,22,7,34,55]
# target = 19

# result = Solution()
# print(result.twoSum(nums,target))

#---------------------------------------------------------------------

#More Optimal Solution

class Solution:
    def twoSum(self,nums,target):
        seen = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff],i]
            seen[num] = i

nums = [12,2,7,51,34]
target = 19

result = Solution()
print(result.twoSum(nums,target))  