class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        pairs = {}
        
        for x in strs:
            key = "".join(sorted(x))
            if key not in pairs:
                pairs[key] = []
            pairs[key].append(x)
                
        return list(pairs.values())