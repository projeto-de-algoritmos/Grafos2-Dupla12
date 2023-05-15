from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for s, d, p in flights:
            graph[s].append((d,p))
        h = [(0, 0, src)]
        visited = set()
        prices = {i: float('inf') for i in range(n)}

        while h:
            price, city, conexao = heappop(h)

            if conexao == dst: return price

            if (conexao, city) in visited or city > k: continue
            visited.add((conexao, city))
            for vizinho, custo in graph[conexao]:
                heappush(h, (price+custo, city + 1, vizinho))
        return -1