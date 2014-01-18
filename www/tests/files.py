import os
import json


def load_file(name):
    currenc_directory = os.path.dirname(__file__)
    path = os.path.join(currenc_directory, name)
    with open(path) as data_file:
        return json.load(data_file)


inital_map_view = load_file('initial_map_view.json')
after_move_map_view = load_file('after_move_map_view.json')
