from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)

    def bfs_least_bus(self, routes, source, target):
        queue = [source]
        buses = 0
        visited_stop = set()
        visited_route = set()
        while queue:
            for _ in range(len(queue)):
                stop = queue.pop(0)
                if stop == target:
                    return buses
                for bus_id in self.graph[stop]:
                    if bus_id not in visited_route:
                        for stop_id in routes[bus_id]:
                            if stop_id not in visited_stop:
                                queue.append(stop_id)
                                visited_stop.add(stop_id)
                    visited_route.add(bus_id)
            buses += 1
        return -1


class Solution:
    def numBusesToDestination(self, routes, source: int, target: int):
        if source == target:
            return 0
        graph = Graph()
        for bus_id, route in enumerate(routes):
            for route_id in route:
                graph.addEdge(route_id, bus_id)
        return graph.bfs_least_bus(routes, source, target)


# routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
# source = 15
# target = 12
routes = [[1, 2, 7], [3, 6, 7]]
source = 1
target = 6
solve = Solution()
print(solve.numBusesToDestination(routes, source, target))
