class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for i in nums:
        #     count[i] = 1 + count.get(i, 0)

        # for n, c in count.items():
        #     freq[c].append(n)

        # res = []
        # for i in range(len(freq)-1, 0 , -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        heap = []
        counter = Counter(nums)

        for i, j in counter.items():
            heapq.heappush(heap, (j, i))
            if len(heap) > k:
                heapq.heappop(heap)

        return [i for j, i in heap]