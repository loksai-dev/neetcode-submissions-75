from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs: # act 
            key = "".join(sorted(word)) #"".join(['a','c','t'])
            groups[key].append(word) #group[act].append(act)

        return list(groups.values())

        