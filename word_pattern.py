class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()
        pattern_key = list(pattern)
        if len(words)!=len(pattern_key):
            return False

        mapping = {}
        for i in range(len(pattern_key)):
            if pattern_key[i] not in mapping:

                if words[i] in mapping.values():
                    return False
                mapping[pattern_key[i]] = words[i]
            else:
                if mapping[pattern_key[i]] != words[i]:
                    return False
                    
        else:
            return True





    

                
