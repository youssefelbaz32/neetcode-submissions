# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

        # def reverse (prev, curr):
        
        #     if not curr:
        #         return prev

        #     temp = curr.next
        #     curr.next = prev

        #     reverse(curr, temp)
        #     return curr

        

        # return reverse(None, head)




        
