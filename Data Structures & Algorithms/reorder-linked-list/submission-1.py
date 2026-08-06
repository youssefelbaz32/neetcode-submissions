# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #we can use a fast pointer and a slow pointer to find half way point

        slow_ptr,fast_ptr = head, head.next

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        """while head.val != slow_ptr.val:
            stored_small = head.next
            stored_big = 
            head.next = fast_ptr"""
        

        fast_ptr = slow_ptr.next
        slow_ptr.next = None
        curr = fast_ptr
        prev = None
        #reverse second half of list:
        while curr:
            stored = curr.next
            curr.next = prev
            prev = curr
            curr = stored



        while prev and head:
            temp = head.next
            temp2 = prev.next

            head.next = prev
            prev.next = temp

            head = prev.next
            prev = temp2


            
            

        