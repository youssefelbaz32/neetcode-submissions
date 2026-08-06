# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mini = list1
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        

        if list1.val <= list2.val:
            mini = list1
            list1 = list1.next
        else:
            mini = list2
            list2 = list2.next
        
        og = mini

        while list1 and list2:
            if list1.val <= list2.val:
                mini.next = list1
                list1 = list1.next
                mini = mini.next
            else:
                mini.next = list2
                list2 = list2.next
                mini = mini.next
        
        while list1:
            mini.next = list1
            list1 = list1.next
            mini = mini.next
        while list2:
            mini.next = list2
            list2 = list2.next
            mini = mini.next
        
        return og



