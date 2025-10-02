
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

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