def swapNodes(head, k):
        cur = head
        
        for i in range(k - 1):
            cur = cur.next
        
        left = cur
        right = head
        while cur.next: 
            cur = cur.next
            right = right.next 
        left.val, right.val = right.val, left.val
        
        return head

swapNodes([1, 2, 3, 4, 5], 2)