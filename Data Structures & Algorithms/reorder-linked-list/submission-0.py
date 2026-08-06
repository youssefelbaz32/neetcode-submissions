# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr = head
        length = 0

        while head:
            length += 1
            head = head.next

        head = curr

        start = curr

        prev = curr
        beginning = curr

        indicator = -1

        if length % 2 == 0:
            indicator = length // 2 -1
        else:
            indicator = length //2

        for moves in range(indicator):
            while head.next:
                prev = head
                head = head.next
                #at end of loop, head becomes 6
                # prev becomes 5
            
            # store = 1
            #start = 0
            #head = 6
            # prev = 5

            store = start.next # 1
            start.next = head
            prev.next = None
            if start.next:
                start.next.next = store
        
            

            start = store
            head = start


        return beginning





        
        


        



        