# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        queue = deque(lists)
        while len(queue) > 1:
            dummy = ListNode()
            head = dummy

            l1 = queue.popleft()
            l2 = queue.popleft()
            while l1 and l2:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                
                head = head.next

            if l1:
                head.next = l1
            else:
                head.next = l2
            
            queue.append(dummy.next)

        return queue[0]