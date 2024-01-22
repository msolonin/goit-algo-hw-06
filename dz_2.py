# -*- coding: utf-8 -*-
"""
Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у
першому завданні.
Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах.
Поясніть, чому шляхи для алгоритмів саме такі.
"""

import networkx as nx
from queue import Queue
from collections import deque
from dz_1 import City, CITY_PATH


def bfs_algorithm(graph, start, end):
    visited = set()
    queue = Queue()
    queue.put((start, [start]))
    while not queue.empty():
        current_node, path = queue.get()
        if current_node == end:
            return path
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.put((neighbor, new_path))
    return None


def dfs_algorithm(graph, start, end):
    visited = set()
    stack = deque([(start, [start])])
    while stack:
        current_node, path = stack.pop()
        if current_node == end:
            return path
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in reversed(list(graph.neighbors(current_node))):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append((neighbor, new_path))
    return None


def print_path(path, name, start_node, end_node):
    if path:
        print(f"{name} Шлях з {start_node} до {end_node}: {path}")
    else:
        print(f"{name} Шлях з {start_node} до {end_node} не знайдено.")


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
    bfs_path = bfs_algorithm(graph, start_node, end_node)
    dfs_path = dfs_algorithm(graph, start_node, end_node)
    print_path(bfs_path, "BFS", start_node, end_node)
    print_path(dfs_path, "DFS", start_node, end_node)
    print("Як бачимо різні алгоритми можуть дати відповідно різні розвязки шляху між вершинами.")


if __name__ == "__main__":
    main()
