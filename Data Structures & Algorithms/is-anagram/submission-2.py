class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        s_chars = {}
        t_chars = {}

        for char in s:
            if char not in s_chars:
                s_chars[char] = 1
            s_chars[char] += 1
        
        for char in t:
            if char not in t_chars:
                t_chars[char] = 1
            t_chars[char] += 1

        for char,amount in s_chars.items():
            if char not in t_chars or t_chars[char] != amount:
                return False

        return True

        