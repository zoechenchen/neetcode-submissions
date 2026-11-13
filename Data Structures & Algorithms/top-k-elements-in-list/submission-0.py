class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            map[i] = 1 + map.get(i, 0)
        for num, count in map.items():
            freq[count].append(num)
        ret = []
        for j in range(len(freq) - 1, 0 , -1):
            for n in freq[j]:
                ret.append(n)
                if len(ret) == k:
                    return ret