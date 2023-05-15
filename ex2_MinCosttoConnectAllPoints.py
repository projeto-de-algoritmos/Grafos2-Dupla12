from typing import List

class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))
        self.tamanho = [1] * n
    
    def find(self, i):
        if self.pai[i] != i:
            self.pai[i] = self.find(self.pai[i])
        return self.pai[i]
    
    def union(self, i, j):
        raiz_i, raiz_j = self.find(i), self.find(j)
        if raiz_i == raiz_j:
            return False
        if self.tamanho[raiz_i] < self.tamanho[raiz_j]:
            raiz_i, raiz_j = raiz_j, raiz_i
        self.pai[raiz_j] = raiz_i
        self.tamanho[raiz_i] += self.tamanho[raiz_j]
        return True

class Solution:
    def minCostConnectPoints(self, pontos: List[List[int]]) -> int:
        n = len(pontos)
        arestas = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(pontos[i][0] - pontos[j][0]) + abs(pontos[i][1] - pontos[j][1])
                arestas.append((dist, i, j))
        arestas.sort()
        uf = UnionFind(n)
        custo = 0
        for dist, i, j in arestas:
            if uf.union(i, j):
                custo += dist
        return custo
