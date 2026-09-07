import collections

class TrieNode:
    def __init__(self):
        self.children = {}
        self.entries = [] 

class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)
        
        nodes_by_len = collections.defaultdict(set)
        edges_by_len = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
        
        for o, c, z in zip(original, changed, cost):
            l = len(o)
            nodes_by_len[l].add(o)
            nodes_by_len[l].add(c)
            edges_by_len[l][(o, c)] = min(edges_by_len[l][(o, c)], z)
            
        root = TrieNode()
        min_dists = {}
        
        for l, nodes in nodes_by_len.items():
            sorted_nodes = sorted(list(nodes))
            s_to_i = {s: i for i, s in enumerate(sorted_nodes)}
            k = len(sorted_nodes)
            
            for s, idx in s_to_i.items():
                node = root
                for char in s:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.entries.append((l, idx))
            
            dist = [[float('inf')] * k for _ in range(k)]
            for i in range(k):
                dist[i][i] = 0
            
            for (u, v), w in edges_by_len[l].items():
                if u in s_to_i and v in s_to_i:
                    ui, vi = s_to_i[u], s_to_i[v]
                    dist[ui][vi] = min(dist[ui][vi], w)
                    
            for mid in range(k):
                for i in range(k):
                    if dist[i][mid] == float('inf'): continue
                    for j in range(k):
                        if dist[mid][j] == float('inf'): continue
                        new_dist = dist[i][mid] + dist[mid][j]
                        if new_dist < dist[i][j]:
                            dist[i][j] = new_dist
            
            min_dists[l] = (s_to_i, dist)
            
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        
        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i+1]
                
            node = root
            for j in range(i, n):
                char = source[j]
                if char not in node.children:
                    break
                node = node.children[char]
                
                for length, u_idx in node.entries:
                    if i + length <= n:
                        t_sub = target[i : i+length]
                        
                        if length not in min_dists:
                            continue

                        s_to_i, dist = min_dists[length]
                        
                        if t_sub in s_to_i:
                            v_idx = s_to_i[t_sub]
                            w = dist[u_idx][v_idx]
                            
                            if w != float('inf') and dp[i+length] != float('inf'):
                                dp[i] = min(dp[i], w + dp[i+length])
                                            
        return dp[0] if dp[0] != float('inf') else -1