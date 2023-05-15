class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        arrestas = collections.defaultdict(list) #lista de adjacencia
        for u, v, w in times:
            arrestas[u].append((v,w)) # v = vizinho // w = peso
        
        minHeap = [(0, k)] #startando a heap
        visitado = set() #monitorando todos os nos que visitamos
        tempo = 0 # resultado

        #Logica de Dijkstra
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visitado:
                continue
            visitado.add(n1) # adcionar como visitiado
            tempo = max(tempo, w1) # increase tempo
            for n2, w2 in arrestas[n1]:
                if n2 not in visitado:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return tempo if len(visitado) == n else -1
