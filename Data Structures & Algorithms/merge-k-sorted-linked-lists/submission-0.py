# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #queue = deque(lists)
        while len(lists) > 1:
            dummy = ListNode()
            head = dummy

            l1 = lists.pop()
            l2 = lists.pop()
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
            
            lists.append(dummy.next)

        return lists[0] if lists else None