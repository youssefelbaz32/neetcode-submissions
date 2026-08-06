class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict_words = defaultdict(list)


        for s in strs:
            s_sorted = ''.join(sorted(s))
            
            dict_words[s_sorted].append(s)
        

        return list(dict_words.values())

        