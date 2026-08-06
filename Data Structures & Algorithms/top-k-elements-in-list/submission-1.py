class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []


        count = Counter(nums)
        ans = []

        for item, priority in count.items():
            heapq.heappush(heap, (-1 * priority, item))

        
        while k:
            key, value = heapq.heappop(heap)
            ans.append(value)
            k -= 1
        
        return ans
        