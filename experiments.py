from re import search
from assign_01 import index_files
from indexer.util.timer import timer
from indexer.sortedarr.sortedarray import SortedArray
from indexer.linkedlist.linklist import LinkedList
from indexer.maps.hash_map import HashMapIndex
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
import uuid
import pandas as pd
import pickle
from searchset import generate_search_set

@timer
def experiment(df, structure, search, com_type, mem_size, index_type, n):
    """
    Parameters: Takes in df for experiment data, indexing structure, search set, and experiment data points

    Does: Searches for each token in the searching set to see if its in the indexing structure, records all the data
    points from the experiment and then appends the data to our df
    """
    uniquedocs = set()
    num_tokens = len(search)
    uniqueid = df.shape[0] + 1
    for term in search:
        docs = structure.search(term)
        for doc in docs:
            uniquedocs.add(doc)

    new_row = {
        "run_id": uniqueid,
        "compute_proc_type": com_type,
        "primary_memory_size": mem_size,
        "index_type": index_type,
        "num_docs_indexed": len(uniquedocs),
        "num_tokens_indexed": num_tokens,
        "search_set_base_size": n,
        "search_time (ns)": 00
    }
    print(new_row)
    return df._append(new_row, ignore_index=True)


def access_pickle(file_name):
    """" Access previously pickled info using given file name"""
    with open(file_name, "rb") as file:
        return pickle.load(file)


def run_experiments(df, structures, avl, com_type, mem_size):

    length_lst = [4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]
    sets = generate_search_set(length_lst, avl)
    snames = ['AVL Tree', 'Sorted Array', 'BST', 'Hash Map', 'Linked List']
    counter = 0

    # Running experiments on all structures and sets
    for i in range(5):
        for k in range(8):
            for j in range(5):
                df, search_time = experiment(df, structures[i], sets[k], com_type, mem_size, snames[i], length_lst[k])
                df.loc[counter, "search_time (ns)"] = search_time
                counter += 1

    uniquedocs = set()
    for term in sets[0]:
        docs = structures[0].search(term)
        for doc in docs:
            uniquedocs.add(doc)

    return df, uniquedocs


def main():
    # Creating df to be turned into our experiment csv
    columns = [
        "run_id",
        "compute_proc_type",
        "primary_memory_size",
        "index_type",
        "num_docs_indexed",
        "num_tokens_indexed",
        "search_set_base_size",
        "search_time (ns)"
    ]
    df = pd.DataFrame(columns=columns)

    # Running experiments
    pickles = ['/Users/michaelmaaseide/Desktop/avl_index.pkl','/Users/michaelmaaseide/Desktop/sortarr.pkl',
               '/Users/michaelmaaseide/Desktop/bst_index.pkl']
    structures = []
    for pickle in pickles:
        structure = access_pickle(pickle)
        structures.append(structure)

    data_directory = '/Users/michaelmaaseide/Desktop/USFinancialNewsArticles-preprocessed'
    hash_index = HashMapIndex(250049)
    index_files(data_directory, hash_index)
    structures.append(hash_index)

    ll_index = LinkedList()
    index_files(data_directory, ll_index, restriction = 1)
    structures.append(ll_index)

    df, doclist = run_experiments(df, structures, pickles[0],'M2 Max', 32)
    print(df)

    with open("timing_data/doclist_for_AVL_searchset1.txt", "w") as file:
        file.writelines(f"{item}\n" for item in doclist)

    df.to_csv('timing_data.csv', index=False)


if __name__ == "__main__":
    main()