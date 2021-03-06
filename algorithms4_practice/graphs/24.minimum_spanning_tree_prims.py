# import sys
# from collections import defaultdict
#
# def PrimsAlgorithm(l):
#
#     nodePosition = []
#     def getPosition(vertex):
#         return nodePosition[vertex]
#
#     def setPosition(vertex, pos):
#         nodePosition[vertex] = pos
#
#     def topToBottom(heap, start, size, positions):
#         if start > size // 2 - 1:
#             return
#         else:
#             if 2 * start + 2 >= size:
#                 m = 2 * start + 1
#             else:
#                 if heap[2 * start + 1] < heap[2 * start + 2]:
#                     m = 2 * start + 1
#                 else:
#                     m = 2 * start + 2
#             if heap[m] < heap[start]:
#                 temp, temp1 = heap[m], positions[m]
#                 heap[m], positions[m] = heap[start], positions[start]
#                 heap[start], positions[start] = temp, temp1
#
#                 temp = getPosition(positions[m])
#                 setPosition(positions[m], getPosition(positions[start]))
#                 setPosition(positions[start], temp)
#
#                 topToBottom(heap, m, size, positions)
#
#     # Update function if value of any node in min-heap decreases
#     def bottomToTop(val, index, heap, position):
#         temp = position[index]
#
#         while(index != 0):
#             if index % 2 == 0:
#                 parent = int( (index-2) / 2 )
#             else:
#                 parent = int( (index-1) / 2 )
#
#             if val < heap[parent]:
#                 heap[index] = heap[parent]
#                 position[index] = position[parent]
#                 setPosition(position[parent], index)
#             else:
#                 heap[index] = val
#                 position[index] = temp
#                 setPosition(temp, index)
#                 break
#             index = parent
#         else:
#             heap[0] = val
#             position[0] = temp
#             setPosition(temp, 0)
#
#     def heapify(heap, positions):
#         start = len(heap) // 2 - 1
#         for i in range(start, -1, -1):
#             topToBottom(heap, i, len(heap), positions)
#
#     def deleteMinimum(heap, positions):
#         temp = positions[0]
#         heap[0] = sys.maxsize
#         topToBottom(heap, 0, len(heap), positions)
#         return temp
#
#     visited = [0 for i in range(len(l))]
#     Nbr_TV  = [-1 for i in range(len(l))] # Neighboring Tree Vertex of selected vertex
#     # Minimum Distance of explored vertex with neighboring vertex of partial tree formed in graph
#     Distance_TV = [] # Heap of Distance of vertices from their neighboring vertex
#     Positions = []
#
#     for x in range(len(l)):
#         p = sys.maxsize
#         Distance_TV.append(p)
#         Positions.append(x)
#         nodePosition.append(x)
#
#     TreeEdges = []
#     visited[0] = 1
#     Distance_TV[0] = sys.maxsize
#     for x in l[0]:
#         Nbr_TV[ x[0] ] = 0
#         Distance_TV[ x[0] ] = x[1]
#     heapify(Distance_TV, Positions)
#
#     for i in range(1, len(l)):
#         vertex = deleteMinimum(Distance_TV, Positions)
#         if visited[vertex] == 0:
#             TreeEdges.append((Nbr_TV[vertex], vertex))
#             visited[vertex] = 1
#             for v in l[vertex]:
#                 if visited[v[0]] == 0 and v[1] < Distance_TV[ getPosition(v[0]) ]:
#                     Distance_TV[ getPosition(v[0]) ] = v[1]
#                     bottomToTop(v[1], getPosition(v[0]), Distance_TV, Positions)
#                     Nbr_TV[ v[0] ] = vertex
#     return TreeEdges
#
# if __name__ == "__main__":
    # < --------- Prims Algorithm --------- >

from algorithms4.graphs import minimum_spanning_tree_prims
from collections import defaultdict
"""
g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
5
14
0 1 2
0 3 6
1 0 2
1 2 3
1 3 8
1 4 5
2 1 3
2 4 7
3 0 6
3 1 8
3 4 9
4 1 5
4 2 7
4 3 9

            
            
            
 Edge   Weight
0 - 1    2
1 - 2    3
0 - 3    6
1 - 4    5


"""
n = int(input("Enter number of vertices: ").strip())
e = int(input("Enter number of edges: ").strip())
adjlist = defaultdict(list)
for x in range(e):
    l = [int(x) for x in input().strip().split()]
    adjlist[l[0]].append([ l[1], l[2] ])
    adjlist[l[1]].append([ l[0], l[2] ])
print(minimum_spanning_tree_prims.PrimsAlgorithm(adjlist))
