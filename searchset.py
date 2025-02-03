import random
from assign_01 import access_pickle
from indexer.util.timer import timer

@timer
def generate_search_set(n, data_directory):
    """
    Generate a search set using indexed terms with the given contraints a,b,c,d
    Returns a shuffled list of the terms
    """
    pickled = access_pickle(data_directory)
    keys = pickled.get_keys()

    search_sets = []
    for i in range(8):
        component_a = random.sample(keys, n)
        component_b = [''.join(random.sample(component_a, random.choice([2, 3]))) for i in range(n // 4)]
        component_c = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8)) for i in range(n)]
        component_d = [' '.join(random.sample(component_c, random.choice([2, 3]))) for i in range(n // 4)]

        search_set = component_a + component_b + component_c + component_d
        random.shuffle(search_set)
        search_sets.append(search_set)

    return search_sets
