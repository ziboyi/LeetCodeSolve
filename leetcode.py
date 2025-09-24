from typing import List, Optional
import re

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 165.比较版本号
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(i) for i in version1.split('.')]
        version2 = [int(i) for i in version2.split('.')]
        if len(version1) > len(version2):
            version2 += [0] * (len(version1) - len(version2))
        elif len(version1) < len(version2):
            version1 += [0] * (len(version2) - len(version1))
        result = 0
        for i, j in zip(version1, version2):
            if i < j:
                result = -1
                break
            elif i > j:
                result = 1
                break
            else:
                continue
        return result

    # 1. 两数之和
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_i, i in enumerate(nums[:-1]):
            for idx_j, j in enumerate(nums[idx_i+1:]):
                if i + j == target:
                    return [idx_i, idx_i+1+idx_j]

    # 10.正则表达式匹配
    def isMatch(self, s: str, p: str) -> bool:
        match = re.match(p, s)
        if match:
            if match.group(0) == s:
                return True
            else:
                return False
        else:
            return False

    # 41. 缺失的第一个正数
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 去除重复的数字并排序
        nums = list(set(nums))
        nums = sorted(nums)
        pos = 0

        # 找到最小的正整数在数组中的位置pos
        for idx, i in enumerate(nums):
            if i <= 0:
                continue
            pos = idx
            break

        # 丢弃pos之前的数，新数组应为[1,2,3,...]，通过比对找出缺失的正整数
        for idx, i in enumerate(nums[pos:]):
            if i != idx + 1:
                return idx + 1
        return nums[-1] + 1


    # 4. 寻找2个正序数组的中位数
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        pos1, pos2 = 0, 0
        nums = []
        len_nums = int(length / 2) + 1
        while len(nums) < len_nums:
            if pos1 >= len(nums1):
                nums += nums2[pos2:]
                break
            if pos2 >= len(nums2):
                nums += nums1[pos1:]
                break
            if nums1[pos1] < nums2[pos2]:
                nums.append(nums1[pos1])
                pos1 += 1
            else:
                nums.append(nums2[pos2])
                pos2 += 1
        if length % 2 == 1:
            return nums[len_nums-1]
        else:
            return (nums[len_nums-2] + nums[len_nums-1]) / 2

    # 23. 合并K个升序链表
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for i in lists: # 循环读取链表并把数值加入到列表l中
            p = i
            while p:
                l.append(p.val)
                p = p.next
        l = sorted(l)
        if not l:
            return None
        node = ListNode(l[0])
        p = node
        for i in l[1:]:
            p.next = ListNode(i)
            p = p.next
        return node

    # 11. 盛最多水的容器
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for idx_i, i in enumerate(height):
            for idx_j, j in enumerate(height[idx_i+1:]):
                area = min([i, j]) * (idx_j + 1)
                if area > max_area:
                    max_area = area
        return max_area



if __name__ == '__main__':
    # result = Solution().compareVersion("1.0.1", "1")
    # result = Solution().twoSum([2,7,11,15], 9)
    # result = Solution().isMatch("aa", "a")
    # result = Solution().firstMissingPositive([7,8,9,11,12])
    # result = Solution().findMedianSortedArrays([1,2,5], [3,4,5])
    result = Solution().maxArea([1,1])
    print(result)