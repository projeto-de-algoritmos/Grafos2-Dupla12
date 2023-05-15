import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for s, d, p in flights:
            graph[s].append((d, p))

        heap = [(0, src, k)]
        prices = {i: float('inf') for i in range(n)}

        while heap:
            price, city, conexao = heapq.heappop(heap)

            if city == dst:
                return price

            if conexao >= 0:
                for neighbor, cost in graph[city]:
                    if price + cost < prices[neighbor]:
                        prices[neighbor] = price + cost
                        heapq.heappush(heap, (price + cost, neighbor, conexao - 1))

        return -1