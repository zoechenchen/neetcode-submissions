class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map = {} 
        # for a in strs:
        #     if tuple(sorted(a)) in map.keys():
        #         map[tuple(sorted(a))].append(a)
        #     else: 
        #         map[tuple(sorted(a))] = [a]
        # return list(map.values())

        map = defaultdict(list)

        for s in strs: 
            count = [0] * 26

            for char in s: 
                count[ord(char)-ord('a')] += 1

            map[tuple(count)].append(s)

        return list(map.values())