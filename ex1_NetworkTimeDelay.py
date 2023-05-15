class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list) #lista de adjacencia
        for u, v, w in times:
            edges[u].append((v,w)) # v = vizinho // w = peso
        
        minHeap = [(0, k)] #startando a heap
        visit = set() #monitorando todos os nos que visitamos
        tempo = 0 # resultado
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1) # adcionar como visitiado
            tempo = max(tempo, w1) # increase tempo

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return tempo if len(visit) == n else -1
