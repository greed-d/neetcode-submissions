class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def counter_map(input_str):
            counter = {}
            for i in range(len(input_str)):
                counter[input_str[i]] = 1 + counter.get(input_str[i], 0)

            return counter

        str_count = {}
        result = []
        counts = []
        for word in strs:
            count = {}
            for ch in word:
                if ch in count:
                    count[ch] += 1
                else:
                    count[ch] = 1
            counts.append(count)

        for str in strs:
            str_count[str] = counter_map(str)

        for i in range(len(strs)):
            word = strs[i]
            value = counts[i]
            found = False
            for group in result:
                if group[0] == value:
                    group[1].append(word)
                    found = True
                    break

            if not found:
                result.append([value, [word]])

        result = [group[1] for group in result]
        return result
