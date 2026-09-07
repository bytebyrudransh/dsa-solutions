class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        from collections import defaultdict, Counter
        
        n = len(source)
        parent = list(range(n))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
        
        for a, b in allowedSwaps:
            union(a, b)
        
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)
        
        mismatches = 0
        for indices in components.values():
            src_count = Counter(source[i] for i in indices)
            for i in indices:
                if src_count[target[i]] > 0:
                    src_count[target[i]] -= 1
                else:
                    mismatches += 1
        
        return mismatches