Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
           
            return (l1 or l2)
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            print(l1.next.val,'l1')
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            print(l2.next.val,'l2')
            return l2
        