class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_1 = list(s)
        anagram_2 = list(t)

        if sorted(anagram_1) == sorted(anagram_2):
            return True
        return False