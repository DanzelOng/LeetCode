class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength, numsSet = 0, set(nums)

        for num in numsSet:
            if num - 1 not in numsSet:
                cnt = 1
                while num + 1 in numsSet:
                    num += 1
                    cnt += 1
                maxLength = max(maxLength, cnt)

        return maxLength   