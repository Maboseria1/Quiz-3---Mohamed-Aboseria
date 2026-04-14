class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        lo, hi, n = min(nums), max(nums), len(nums)
        if lo == hi: return 0

        size = max(1, (hi - lo) // (n - 1))
        k = (hi - lo) // size + 1
        buckets = [[float('inf'), float('-inf')] for _ in range(k)]

        for x in nums:
            b = (x - lo) // size
            buckets[b][0] = min(buckets[b][0], x)
            buckets[b][1] = max(buckets[b][1], x)

        ans, prev = 0, lo
        for bmin, bmax in buckets:
            if bmin == float('inf'): continue
            ans = max(ans, bmin - prev)
            prev = bmax
        return ans
