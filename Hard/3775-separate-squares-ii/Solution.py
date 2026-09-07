class Solution(object):
    def separateSquares(self, squares):
    
        xs = set()
        for x, y, l in squares:
            xs.add(x)
            xs.add(x + l)
        
        sorted_x = sorted(list(xs))
        x_map = {val: i for i, val in enumerate(sorted_x)}
        n_intervals = len(sorted_x) - 1
        
        # If there are no intervals, area is 0
        if n_intervals == 0:
            return 0.0

        count = [0] * (4 * n_intervals)
        total_len = [0.0] * (4 * n_intervals)
        
        # Recursive update function for the Segment Tree
        def update(idx, left, right, q_left, q_right, val):
            if q_left >= right or q_right <= left:
                return
            
            if q_left <= left and right <= q_right:
                count[idx] += val
            else:
                mid = (left + right) // 2
                update(2 * idx, left, mid, q_left, q_right, val)
                update(2 * idx + 1, mid, right, q_left, q_right, val)
            
            # Update length logic for Union of Intervals
            if count[idx] > 0:
                
                total_len[idx] = float(sorted_x[right] - sorted_x[left])
            else:
                # If not fully covered, it's the sum of children
                if right - left == 1:
                    total_len[idx] = 0.0
                else:
                    total_len[idx] = total_len[2 * idx] + total_len[2 * idx + 1]

        # 3. Create Events
        # Format
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        
         
        events.sort(key=lambda e: e[0])
        
        # 4. Sweep Line Process
        strips = [] # Stores 
        prev_y = events[0][0]
        
        i = 0
        n_events = len(events)
        
        while i < n_events:
            curr_y = events[i][0]
            
            # Calculate area of the strip
            if curr_y > prev_y:
                width = total_len[1] # Root of segment tree holds total covered length
                strips.append((prev_y, curr_y - prev_y, width))
            
            # Process all events at the current y height
            while i < n_events and events[i][0] == curr_y:
                _, type_, x1, x2 = events[i]
                l_idx = x_map[x1]
                r_idx = x_map[x2]
                # Update range 
                update(1, 0, n_intervals, l_idx, r_idx, type_)
                i += 1
            
            prev_y = curr_y

        # 5. Calculate Total Area and Find Split Point
        total_area = sum(h * w for _, h, w in strips)
        target = total_area / 2.0
        
        current_area = 0.0
        for y, h, w in strips:
            strip_area = h * w
            if current_area + strip_area >= target:
                # We found the strip containing the split line
                needed = target - current_area
                return y + needed / w
            current_area += strip_area
            
        return float(prev_y)
        