def hasCycle(head):
        fast = head
        slow = head

        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next

            if fast == slow: 
                return True
        
        return False

    # Time => O(n)
    # Space => O(1) 