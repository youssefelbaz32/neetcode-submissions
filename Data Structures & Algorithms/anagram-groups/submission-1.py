class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)


        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())
            




#        dict_words = defaultdict(list)


 #       for s in strs:
 #           s_sorted = ''.join(sorted(s))
            
 #           dict_words[s_sorted].append(s)
        

 #       return list(dict_words.values())

        