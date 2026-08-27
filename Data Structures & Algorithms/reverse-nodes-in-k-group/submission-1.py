# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        save = None
        save_last = None

        while head:
            count = 0
            check_node = head
            while count < k and check_node:
                check_node = check_node.next
                count += 1

            if count < k:
                if save_last:
                    save_last.next = head
                return save

            prev, curr = None, head
            last_node = curr
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            if not save:
                save = prev

            if save_last:
                save_last.next = prev

            save_last = head
            head = curr

        return save

