# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #node = 0, node.next = 1
        #node = 1, node.next = 0
        prev = None
        curr = head
        while curr:
            stored = curr.next
            curr.next = prev
            prev = curr
            curr = stored

        return prev



            
        