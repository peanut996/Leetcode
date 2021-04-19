import collections
from typing import List

"""[summary]
743. 网络延迟时间
有 N 个网络节点，标记为 1 到 N。

给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从源节点传递到目标节点的时间。

现在，我们从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。
"""
def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
    #BFS 解法
    dic = collections.defaultdict(list)
    for u, v, w in times:
        dic[u].append((v, w))
    visited = {K: 0}
    queue = [(K, 0)]
    while queue:
        cnode, ctime = queue.pop(0)
        for nnode, ntime in dic[cnode]:
            t = ctime + ntime
            if nnode not in visited or t < visited[nnode]:
                visited[nnode] = t
                queue.append((nnode, t))
    if len(visited) == N:
        return max(visited.values())
    return -1
