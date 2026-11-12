class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {} 
        for a in strs:
            if tuple(sorted(a)) in map.keys():
                map[tuple(sorted(a))].append(a)
            else: 
                map[tuple(sorted(a))] = [a]
        return list(map.values())