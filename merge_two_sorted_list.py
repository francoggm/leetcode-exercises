# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        if len(list1) <= 50 and len(list2) <= 50:
            list_main, list_secondary = (list1, list2) if len(list1 ) >= len(list2) else (list2, list1)
            new_list = []
            for i, j in enumerate(list_main):
                if i < len(list_secondary):
                    if j <= list_secondary[i]:
                        new_list.extend([j, list_secondary[i]])
                    elif list_secondary[i] < j:
                        new_list.extend([list_secondary[i], j])
                else:
                    return list_main
            new_list.sort()
            return new_list
list1 = []
list2 = [0]

