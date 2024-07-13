def getDecimalValue(head):
        answer = ''

        if head is None:
            return

        temp = head
        while temp is not None:
            answer = answer + str(temp.val)
            temp = temp.next
        
        return int(answer, 2)
