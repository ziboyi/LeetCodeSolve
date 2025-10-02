from typing import List, Optional, Tuple
import re

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



    # 11. 盛最多水的容器
    def maxArea(self, height: List[int]) -> int:
        # 此方法时间复杂度为 O(n^2)，时间复杂度太高
        # max_area = 0
        # for idx_i, i in enumerate(height):
        #     for idx_j, j in enumerate(height[idx_i+1:]):
        #         area = min([i, j]) * (idx_j + 1)
        #         if area > max_area:
        #             max_area = area
        # return max_area

        # 在边缘设置双指针，向内移动对应数值更大的指针只会得到盛水更少的容器，
        # 要得到盛更多水的容器，向内移动对应数值更小的指针即可。
        pos1, pos2 = 0, len(height) - 1
        max_area = 0
        while pos1 < pos2:
            area = min(height[pos1], height[pos2]) * (pos2 - pos1)
            if area > max_area:
                max_area = area
            if height[pos1] < height[pos2]:
                pos1 += 1
            else:
                pos2 -= 1
        return max_area

    # 20. 有效的括号
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in ['}', ')', ']']:
                if len(stack) == 0:
                    return False
                elif stack[-1] == '(' and char == ')':
                    stack = stack[:-1]
                elif stack[-1] == '[' and char == ']':
                    stack = stack[:-1]
                elif stack[-1] == '{' and char == '}':
                    stack = stack[:-1]
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


    def find_last_valid_pairs(self, s: str):
        pos_start, pos_end = 0, 0
        stack = []
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            elif char == ')' and len(stack) > 0:
                pos_start = stack[-1]
                pos_end = idx
                stack = stack[:-1]
        return pos_start, pos_end

    def find_valid_pairs(self, s:str):
        if len(s) == 0:
            return []
        valid_pairs = []
        while True:
            pos_start, pos_end = self.find_last_valid_pairs(s)
            if pos_start == 0 and pos_end == 0:
                break
            else:
                valid_pairs = [(pos_start, pos_end)] + valid_pairs
                s = s[:pos_start]
        new_valid_pairs = []
        for idx, i in enumerate(valid_pairs):
            if len(new_valid_pairs) == 0:
                new_valid_pairs.append(i)
                continue
            if i[0] == new_valid_pairs[-1][1] + 1: #把相邻的pair首尾相接
                new_valid_pairs[-1] = (new_valid_pairs[-1][0], i[1])
            else:
                new_valid_pairs.append(i)
        return new_valid_pairs


    # 32. 最长有效括号
    def longestValidParentheses(self, s: str) -> int:
        valid_pairs = self.find_valid_pairs(s)
        print(valid_pairs)
        max_length = 0
        for i, j in valid_pairs:
            if max_length < j - i + 1:
                max_length = j - i + 1
        return max_length



if __name__ == '__main__':
    # result = Solution().compareVersion("1.0.1", "1")
    # result = Solution().twoSum([2,7,11,15], 9)
    # result = Solution().isMatch("aa", "a")
    # result = Solution().firstMissingPositive([7,8,9,11,12])
    # result = Solution().findMedianSortedArrays([1,2,5], [3,4,5])
    # result = Solution().maxArea([1,8,6,2,5,4,8,3,7])
    # result = Solution().isValid("({")
    result = Solution().longestValidParentheses(')()())')
    print(result)