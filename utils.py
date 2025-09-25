
import numpy as np

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 分解因数，返回排序后的因数列表
def find_factors(n: int) -> list[int]:
    n = abs(int(n))
    factors = []
    divisor = 2
    while n >= divisor:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    return factors

# 求交集
def find_intersection(l1: list, l2: list) -> list:
    return np.intersect1d(l1, l2).tolist()

# 求并集
def find_union(l1: list, l2: list) -> list:
    return np.union1d(l1, l2).tolist()

# 求差集，在集合1中出现，集合2中没出现的值
def find_setdiff(l1: list, l2: list) -> list:
    return np.setdiff1d(l1, l2, assume_unique=True).tolist()