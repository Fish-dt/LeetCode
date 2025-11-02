class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        guarded = set()
        guard_set = {(r, c) for r, c in guards}
        wall_set = {(r, c) for r, c in walls}
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and (nr, nc) not in wall_set and (nr, nc) not in guard_set:
                    guarded.add((nr, nc))
                    nr += dr
                    nc += dc
        
        total_cells = m * n
        occupied = len(guards) + len(walls)
        unguarded = total_cells - occupied - len(guarded)
        return unguarded
        