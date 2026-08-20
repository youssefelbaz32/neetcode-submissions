# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        slow_node = head
        if head.next:
            fast_node = head.next
        else:
            return False

        while slow_node and fast_node:

            if slow_node == fast_node:
                return True
            
            slow_node = slow_node.next
            if fast_node.next:
                fast_node = fast_node.next.next
            else:
                return False
        

        return False

        