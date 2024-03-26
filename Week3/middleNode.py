# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr, double_ptr = head, head
        while double_ptr and double_ptr.next:
            ptr = ptr.next
            double_ptr = double_ptr.next.next
        return ptr