class Solution {
public:
    int minCost(vector<vector<int>>& grid, int k) {
        int n = grid.size();
        int m = grid[0].size();

        using State = tuple<int,int,int,int,int>;
        priority_queue<State, vector<State>, greater<>> pq;
        vector dist(n, vector(m, vector(k+1, vector<int>(5, INT_MAX))));
        
        dist[0][0][0][4] = grid[0][0];
        pq.emplace(grid[0][0], 0, 0, 0, 4);

        vector<int> dr = {-1, 0, 1, 0};
        vector<int> dc = {0, 1, 0, -1};

        while(!pq.empty()) {
            auto [cost, turns, r, c, prevDir] = pq.top();
            pq.pop();
            
            if(cost != dist[r][c][turns][prevDir]) continue;

            if(r == n-1 && c == m-1) return cost;

            for(int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if(nr < 0 || nr >= n || nc < 0 || nc >= m) continue;

                int newTurns = turns;
                if(prevDir != 4 && prevDir != d) newTurns++;
                if(newTurns > k) continue;

                int newCost = cost + grid[nr][nc];
                if(newCost < dist[nr][nc][newTurns][d]) {
                    dist[nr][nc][newTurns][d] = newCost;
                    pq.emplace(newCost, newTurns, nr, nc, d);
                }
            }
        }

        return -1;
    }
};