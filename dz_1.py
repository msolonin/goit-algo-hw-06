# -*- coding: utf-8 -*-
"""
Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (наприклад, транспортної мережі
міста, соціальної мережі, інтернет-топології).
info
Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).
"""

import networkx as nx
import matplotlib.pyplot as plt
import csv
import random

CITY_PATH = [[17, 25, 7, 4, 15, 10, 11], [15, 11], [7, 1, 22], [17, 14, 23, 1], [14, 8, 1], [4, 22, 18, 11],
             [18, 6, 11], [6, 19, 11], [22, 24, 6]]


class City:
    def __init__(self, file_name='city.csv'):
        self.file_name = file_name
        self.all_csv_info = []
        self.all_ids = {}
        self._open_file()
        self._get_all_ids()

    def _open_file(self):
        with open(self.file_name, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            all_cities = []
            for row in spamreader:
                all_cities.append(row)
        self.all_csv_info = all_cities

    def _get_all_ids(self):
        self.all_ids = {f[0]: f[1] for f in self.all_csv_info if f[0]}

    def get_distance(self, city_id_from, city_id_to):
        index = self.all_csv_info[0].index(str(city_id_to))
        for f in self.all_csv_info:
            if f[0] == str(city_id_from):
                return int(f[index])
        return 0

    def get_random_city_data(self, count=None, main_city=None):
        city_data = []
        if [f for f in self.all_csv_info if f[1] == main_city]:
            city_id_from = [f for f in self.all_csv_info if f[1] == main_city][0][0]
        else:
            city_id_from = random.choice(list(self.all_ids.keys()))
            main_city = self.all_ids[city_id_from]
        not_main_city_ids = [f[0] for f in self.all_csv_info if f[0] and f[0] != city_id_from]
        for index, city_id_to in enumerate(not_main_city_ids):
            name_to = self.all_ids[city_id_to]
            distance = self.get_distance(city_id_from, city_id_to)
            city_data.append([main_city, name_to, distance])
            if index >= count:
                return city_data
        return city_data

    def get_path_graph_data(self, paths):
        city_data = []
        for path in paths:
            for index, city_id_from in enumerate(path):
                if index < len(path) - 1:
                    name_from = self.all_ids[str(city_id_from)]
                    city_id_to = str(path[index + 1])
                    name_to = self.all_ids[city_id_to]

                    distance = self.get_distance(str(city_id_from), city_id_to)
                    data = [name_from, name_to, distance]
                    if data not in city_data:
                        city_data.append(data)
        return city_data


def main(count_of_cities=24):
    """ Створюемо граф відстаней між 2-ма містамиб Щоб подивитися як краще до нього доїхати
    """
    city = City()
    graph = nx.Graph()
    # cities = city.get_random_city_data(count_of_cities)
    cities = city.get_path_graph_data(CITY_PATH)
    for city_item in cities:
        graph.add_edge(city_item[0], city_item[1], weight=city_item[2])
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.show()


if __name__ == '__main__':
    main()
