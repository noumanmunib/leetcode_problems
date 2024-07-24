from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.k = 3000

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue[0] < t - self.k:
            self.queue.popleft()

        return len(self.queue)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)