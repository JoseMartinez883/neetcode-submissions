class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        is_prefix = True
        prefix = ""
        first_word = list(strs[0])
        index = 0
        
        while is_prefix:
            if index < len(first_word):
                pre_prefix = first_word[index]
                
                for word in strs:
                    if len(word) <= index or word[index] != pre_prefix :
                        is_prefix = False
                        break
                
                if is_prefix : prefix += pre_prefix
                index += 1
            else:
                is_prefix = False
        
        return prefix