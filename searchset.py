import random
from indexer.trees.avl_tree import AVLTreeIndex
from assign_01 import index_files
from indexer.util.timer import timer
import pickle

def generate_search_set(n, data_directory):
    """
    Generate a search set using indexed terms with the given contraints a,b,c,d
    Returns a shuffled list of the terms
    """
    avl_index = AVLTreeIndex()
    index_files(data_directory, avl_index)
    keys = avl_index.get_keys()

    search_sets = []
    for i in range(8):
        k = n[i]
        component_a = random.sample(keys, k)
        component_b = [''.join(random.sample(component_a, random.choice([2, 3]))) for i in range(k // 4)]
        component_c = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8)) for i in range(k)]
        component_d = [' '.join(random.sample(component_c, random.choice([2, 3]))) for i in range(k // 4)]

        search_set = component_a + component_b + component_c + component_d
        random.shuffle(search_set)
        search_sets.append(search_set)

    return search_sets
