class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for num in nums:
            group[num] = group.get(num,0) + 1

        sorted_values = sorted(group, key = lambda i: group[i], reverse = True)
        return sorted_values[:k]


