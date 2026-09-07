import heapq

class Solution:
    def minCost(self, n, edges):
        graph = [[] for _ in range(n)]
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))
            
        pq = [(0, 0)]
        min_costs = [float('inf')] * n
        min_costs[0] = 0
        
        while pq:
            current_cost, u = heapq.heappop(pq)
            
            if current_cost > min_costs[u]:
                continue
            
            if u == n - 1:
                return current_cost
            
            for v, weight in graph[u]:
                new_cost = current_cost + weight
                if new_cost < min_costs[v]:
                    min_costs[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
                    
        return -1