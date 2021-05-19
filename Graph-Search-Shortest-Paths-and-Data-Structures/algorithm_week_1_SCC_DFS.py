import time
from collections import defaultdict
import sys, threading
sys.setrecursionlimit(3000000)  
threading.stack_size(67108864)  

def dfs(vert):
    global n, vertex_used, vertex_order, l_rev_graph
    vertex_used[vert] = True
    if len(l_rev_graph[vert])>0: 
        for v in l_rev_graph[vert]:
            if not vertex_used[v]:
                dfs(v)
    vertex_order.append(vert)


def scc(vert, n):
    global vertex_used, l_graph
    vertex_used[vert] = True
    if len(l_graph[vert])>0: 
        for v in l_graph[vert]:
            if not vertex_used[v]:
                n = scc(v, n)
    n += 1
    return n

def main():
    global n, vertex_used, vertex_order, l_graph, l_rev_graph
    l_graph     = defaultdict(list)
    l_rev_graph = defaultdict(list)
    f = open("scc.txt", "r")
    for line in f:
        v = line.split()
        v0, v1 = int(v[0]), int(v[1])
        l_graph[v0].append(v1)
        l_rev_graph[v1].append(v0)
    f.close()
    graph_size = max(max(l_graph),max(l_rev_graph))
    vertex_used = {x:False for x in range(1,graph_size+1)}

    vertex_order = list()
    keys = set(l_graph.keys())
    keys = sorted(keys, reverse=True)
    for v in range(1,graph_size+1):
        if not vertex_used[v]:
            dfs(v)
    vertex_order.reverse()

    vertex_used = {x:False for x in range(1,graph_size+1)}

    l_result  = list()

    n = 0
    for v in vertex_order:
        if not vertex_used[v]:
            n = scc(v, n) 
            l_result.append(n)
            n = 0

    l_result.sort(reverse=True)
    # return l_result[0:10]
    print(l_result[0:10])

if __name__ == '__main__':
    start = time.time()
    thread=threading.Thread(target=main)  
    thread.start() 
    print (time.time() - start)