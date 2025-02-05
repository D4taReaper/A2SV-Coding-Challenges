class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        if len(strs) >= 1:
            for i in range(1, len(strs)):
                word = strs[i]
                for j in range(len(prefix)):
                    if j == len(word):
                        prefix = prefix[ : j]
                        break
                    if prefix[j] != word[j]:
                        prefix = prefix[ : j]
                        break
            if prefix:
                return prefix
            else:
                return ""    
        

            

                    

        
