from collections import deque

def deckRevealedIncreasing(deck):
        deck.sort()
        res = [0] * len(deck)

        queue = deque(range(len(deck)))

        for c in deck:
            i = queue.popleft()
            res[i] = c

            if queue:
                queue.append(queue.popleft()) # pop and shift it to the end of queue

        return res

# Time -> O(nlogn)
# Space -> O(n)
