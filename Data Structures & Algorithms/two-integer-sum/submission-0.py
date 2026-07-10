class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic_value = {}
        for key, value in enumerate(nums):
            complement = target - value

            if complement in dic_value:
                return [dic_value[complement], key]

            dic_value[value] = key
