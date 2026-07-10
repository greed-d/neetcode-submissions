class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for num in nums:
            if num in group:
                group[num] = 1 + group.get(num, 0)
            else:
                group[num] = 1

        result = []
        sorted_group = {
            key: value
            for key, value in sorted(
                group.items(), key=lambda item: item[1], reverse=True
            )
        }
        sliced_dict = dict(list(sorted_group.items())[:k])

        result.extend(int(key) for key, value in sliced_dict.items())

        return result

