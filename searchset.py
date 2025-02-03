import random
import string
from indexer.trees.avl_tree import AVLTreeIndex
from assign_01 import index_files
import pickle

def generate_search_set_pickle(n, data_directory):
    """
    Generate a search set using indexed terms with the given contraints a,b,c,d
    Returns a shuffled list of the terms
    """
    with open(data_directory, "rb") as file:
        pickled = pickle.load(file)
        keys = pickled.get_keys()

    search_sets = []
    for i in range(8):
        component_a = random.sample(keys, n)
        component_b = [''.join(random.sample(component_a, random.choice([2, 3]))) for i in range(n // 4)]
        component_c = [''.join(random.choices('qwertyuiopasdfghjklzxcvbnm', k=8)) for i in range(n)]
        component_d = [' '.join(random.sample(component_c, random.choice([2, 3]))) for i in range(n // 4)]

        search_set = component_a + component_b + component_c + component_d
        random.shuffle(search_set)
        search_sets.append(search_set)

    return search_sets
def main():

    # data_directory = '/Users/michaelmaaseide/desktop/USFinancialNewsArticles-preprocessed'
    data_directory = r"C:\Users\samba\OneDrive\Desktop\DS 4300 Large Scale Info\avl_index.pkl"
    search_sets = generate_search_set_pickle(4000, data_directory)
    print(search_sets)



if __name__ == '__main__':
    main()