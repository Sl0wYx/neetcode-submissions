# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, prev_rvrs1 = head, None

        while curr:
            nxt = curr.next
            curr.next = prev_rvrs1
            prev_rvrs1 = curr
            curr = nxt

        rvrsd = prev_rvrs1
        point = rvrsd
        prev_rmv = None
        count = 1
        while count < n:
            prev_rmv = point
            point = point.next
            count += 1  
        if prev_rmv == None:
            rvrsd = point.next
        else:
            nxt = point.next
            prev_rmv.next = nxt
            
        curr, prev = rvrsd, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev