from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = head
        prev = None
        curr = head

        while curr is not None and curr.next is not None:
            following = curr.next
            tail = following.next

            following.next = curr
            curr.next = tail

            if prev is not None:
                prev.next = following
            else:
                new_head = following

            prev = curr
            curr = tail

        return new_head


s = Solution()
head = None
result = s.swapPairs(head)
print(result)