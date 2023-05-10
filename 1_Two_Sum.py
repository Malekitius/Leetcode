class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            hashmap[val] = i
        for i, val in enumerate(nums):
            complement = target - val
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]