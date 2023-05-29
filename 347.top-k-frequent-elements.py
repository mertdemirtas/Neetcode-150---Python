#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        
        for element in nums:
            dic[element] = 1 + dic.get(element, 0)
        
        heap = []

        for key, value in dic.items():
            heap.append([-value, key])
        heapq.heapify(heap)
        res = []
        for i in range(k):
            value, key = heapq.heappop(heap)
            res.append(key)
        return res
# @lc code=end

