class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        count = 1
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = count
            else:
                seen[nums[i]] += count
        return sorted(seen, key= seen.get, reverse=True)[:k]
