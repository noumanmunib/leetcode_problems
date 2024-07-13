def removeElements(head, val):
        if not head: 
            return 

        dummy = cur = ListNode(0)
        dummy.next = head

        while cur:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next

        return dummy.next 