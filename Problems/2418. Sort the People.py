from collections import heapq

def sortPeople(names, heights):
        pq = []

        for i in range(len(names)):
            heapq.heappush(pq, (-heights[i], names[i])) # Use negative heights to simulate a max-heap

        for i in range(len(names)):
            names[i] = heapq.heappop(pq)[1]
        
        return names
