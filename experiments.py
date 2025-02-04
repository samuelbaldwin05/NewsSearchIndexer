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

    num_tokens = len(search)
    uniqueid = df.shape[0] + 1
    search_base_set_size = len(structure.get_keys())
    num_docs = 0
    for term in search:
        doc_list = structure.search(term)
        if doc_list:
            num_docs += len(doc_list)

    new_row = {
        "run_id": uniqueid,
        "compute_proc_type": com_type,
        "primary_memory_size": mem_size,
        "index_type": index_type,
        "num_docs_indexed": num_docs,
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


def run_experiments(df, pickles, com_type, mem_size):
    structures = []
    for pickle in pickles:
        structure = access_pickle(pickle)
        structures.append(structure)

    length_lst = [4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]
    sets = generate_search_set(length_lst, pickles[0])

    # Running experiments on all structures and sets
    for i in range(4):
        for k in range(8):
            for j in range(5):
                df, search_time = experiment(df, structures[i], sets[k], com_type, mem_size, 'AVL', length_lst[k])
                df.loc[df.index[-1], "search_time (ns)"] = search_time

    return df


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

    # Getting indexing structure into file
    # pickle_data = '/Users/michaelmaaseide/Desktop/avl_index.pkl'
    # # pickle_data = r"C:\Users\samba\OneDrive\Desktop\DS 4300 Large Scale Info\avl_index.pkl"
    # avl = access_pickle(pickle_data)
    #
    # # Creating searching sets
    # length_lst = [4000,5000,6000,7000,8000,9000,10000,11000]
    # sets = generate_search_set(length_lst, pickle_data)
    # print(len(sets))
    # print(len(sets[0]))
    # data = r"C:\Users\samba\OneDrive\Desktop\DS 4300 Large Scale Info\bst_index.pkl"
    # Running experiment on searching set one time


    # new_df, search_time = experiment(df, avl, sets[0], 'M2 Max', 32, 'AVL', length_lst[0])
    # new_df.loc[new_df.index[-1], "search_time (ns)"] = search_time
    #
    # print(new_df.head())

    # Running experiments
    pickles = ['/Users/michaelmaaseide/Desktop/avl_index.pkl','/Users/michaelmaaseide/Desktop/sortarr.pkl',
               '/Users/michaelmaaseide/Desktop/bst_index.pkl','/Users/michaelmaaseide/Desktop/hashindex.pkl']
    run_experiments(df, pickles, 'M2 Max', 32)


if __name__ == "__main__":
    main()