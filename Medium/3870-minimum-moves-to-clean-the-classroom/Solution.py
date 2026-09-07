from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        R, C = len(classroom), len(classroom[0])
        litter_map = {}
        
        for r in range(R):
            for c in range(C):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = len(litter_map)
                    
        num_litter = len(litter_map)
        if not num_litter: 
            return 0
            
        target_mask = (1 << num_litter) - 1
        vis = [[[-1] * C for _ in range(R)] for _ in range(1 << num_litter)]
        vis[0][sr][sc] = energy
        
        q = deque([(0, sr, sc, 0, energy)])
        
        while q:
            moves, r, c, mask, e = q.popleft()
            
            if mask == target_mask:
                return moves
            
            if e == 0:
                continue
                
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < R and 0 <= nc < C and classroom[nr][nc] != 'X':
                    ne, nmask = e - 1, mask
                    
                    if classroom[nr][nc] == 'L':
                        nmask |= (1 << litter_map[(nr, nc)])
                    elif classroom[nr][nc] == 'R':
                        ne = energy
                        
                    if ne > vis[nmask][nr][nc]:
                        vis[nmask][nr][nc] = ne
                        q.append((moves + 1, nr, nc, nmask, ne))
                        
        return -1