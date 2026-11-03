import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        dist=[]
        for i in range(m):
            row=[float('inf')]*n
            dist.append(row)
        dist[0][0]=0
        min_heap=[(0,0,0)]
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        while min_heap:
            curr_dist,r,c=heapq.heappop(min_heap)
            if curr_dist > dist[r][c]:
                continue
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<m and 0<=nc<n:
                    new_dist=max(curr_dist,abs(heights[r][c]-heights[nr][nc]))
                    if new_dist < dist[nr][nc]:
                        dist[nr][nc]=new_dist
                        heapq.heappush(min_heap,(new_dist,nr,nc))
            if r==m-1 and c==n-1:
                return curr_dist
