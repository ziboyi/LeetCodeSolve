
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

    # 2. 两数相加
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        n1, n2 = 0, 0
        e1, e2 = 1, 1
        while p1 != None:
            n1 += p1.val * e1
            e1 *= 10
            p1 = p1.next
        while p2 != None:
            n2 += p2.val * e2
            e2 *= 10
            p2 = p2.next
        n = n1 + n2
        digit_list = [int(i) for i in str(n)]
        l = ListNode(val=digit_list.pop(), next=None)
        p = l
        while len(digit_list) > 0:
            p.next = ListNode(val=digit_list.pop(), next=None)
            p = p.next
        return l

    # 25. K个一组翻转链表
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = []
        p = head
        while p != None:
            l.append(p.val)
            p = p.next

        last_numbers = []
        if len(l) % k != 0:
            last_numbers = l[-(len(l) % k):]

        reversed_l = []
        group = []
        for idx, i in enumerate(l):
            group.append(i)
            if len(group) % k == 0:
                group.reverse()
                reversed_l += group
                group = []
        reversed_l += last_numbers

        head = ListNode()
        p = head
        for i in reversed_l:
            p.next = ListNode(i)
            p = p.next
        head = head.next
        return head






if __name__ == '__main__':
    result = Solution().test([1,2,3,4,5], 3)
    print(result)