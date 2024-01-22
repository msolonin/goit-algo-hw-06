# -*- coding: utf-8 -*-
"""
Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі:
додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.
"""


import networkx as nx
from dz_1 import City, CITY_PATH
from dz_2 import print_path
import heapq


def dijkstra_algorithm(graph, start, end):
    distances = {node: float('infinity') for node in graph.nodes}
    predecessors = {node: None for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node == end:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = predecessors[current_node]
            return path
        if current_distance > distances[current_node]:
            continue
        for neighbor, edge_data in graph[current_node].items():
            weight = edge_data['weight']
            distance_to_neighbor = distances[current_node] + weight

            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))
    return None


def main():
    graph = nx.Graph()
    city = City()
    cities = city.get_path_graph_data(CITY_PATH)
    # Створення графу з вагами ребер
    for city_item in cities:
        graph.add_edge(city_item[0], city_item[1], weight=city_item[2])
    # Знаходження шляху між вершинами '17' та '11' Суми - Львів
    start_node = 'Суми'
    end_node = 'Львів'
    dijkstra_path = dijkstra_algorithm(graph, start_node, end_node)
    print_path(dijkstra_path, "Дейкстри", start_node, end_node)


if __name__ == "__main__":
    main()
