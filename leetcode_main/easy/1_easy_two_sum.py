class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List = []
        for i in range(len(nums)):  # range(len(nums)来循环列表索引
            ni = nums[i]
            n = target - ni
            for j in range(len(nums)):
                nj = nums[j]
                if nj == n and j > i:
                    List.append(i)  # .append()为列表增加元素
                    List.append(j)
                    break
        return List
