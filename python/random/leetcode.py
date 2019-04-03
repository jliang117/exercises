graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def doubleAssign(graph,start):
    stack = [(start,[start])]
    print(stack)
    (vertex,path) = stack.pop()
    print(vertex)
    print(path)

doubleAssign(graph,'A')

from collections import deque
def bfs(graph, start):
    visited, dQueue = set(), deque(start)
    while dQueue:
        vertex = dQueue.popleft()
        print('vert:%s' % vertex)
        if vertex not in visited:
            visited.add(vertex)
            dQueue.extend(graph[vertex]-visited)
            print(dQueue)
    return visited



def bfsList(graph, start):
    visited, queue = set(),[start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)
    return visited

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        print('vert:%s' % vertex)
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
            print(stack)
    return visited

# print(dfs(graph,'A'))
# print(bfsList(graph,'A'))

