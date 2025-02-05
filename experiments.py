from re import search
import uuid
import pandas as pd
import pickle

from assign_01 import index_files
from indexer.util.timer import timer
from searchset import generate_search_set

# Structures
from indexer.sortedarr.sortedarray import SortedArray
from indexer.linkedlist.linklist import LinkedList
from indexer.maps.hash_map import HashMapIndex
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.trees.bst_index import BinarySearchTreeIndex

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

def index_all(data_directory):
    """ Given a data directory index it using all the structures, returning a list of the indexed
    structures """
    structures = []
    hash_index = HashMapIndex(250049)  # This value is the capacity of the hashmap
    index_files(data_directory, hash_index)
    structures.append(hash_index)

    ll_index = LinkedList()
    index_files(data_directory, ll_index, count=8000)  # We used count 8000 as the full dataset took too long
    structures.append(ll_index)

    avl_index = AVLTreeIndex()
    index_files(data_directory, avl_index)
    structures.append(avl_index)

    bst_index = BinarySearchTreeIndex()
    index_files(data_directory, bst_index)
    structures.append(bst_index)

    sorted_array_index = SortedArray()
    index_files(data_directory, sorted_array_index)
    structures.append(sorted_array_index)

    return structures

def run_experiments(df, structures, data_directory, com_type, mem_size):
    """ Given dataframe, structures, avl, computer type, and memory size, create the search sets
    using the avl tree, then run the experiments
    for each of the 5 structures, and for each of the 8 length sizes, each 5 times to reduce error.
    Update the data frame along the way, and return the final dataframe as well as a specific search
    result set
    """
    length_lst = [4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]
    sets = generate_search_set(length_lst, data_directory)
    snames = ['AVL Tree', 'Sorted Array', 'BST', 'Hash Map', 'Linked List']
    counter = 0

    # Running experiments on all structures and sets
    for i in range(5):
        for k in range(8):
            for j in range(5):
                df, search_time = experiment(df, structures[i], sets[k], com_type, mem_size, snames[i], length_lst[k])
                df.loc[counter, "search_time (ns)"] = search_time
                counter += 1

    # Get specific search result
    uniquedocs = set()
    for term in sets[0]:
        docs = structures[0].search(term)
        for doc in docs:
            uniquedocs.add(doc)

    return df, uniquedocs


def main():
    # Creating empty df to be turned into our experiment csv
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

    # ONLY SPOT THAT NEEDS INPUT!!!!!!!!
    # data_directory = '/Users/michaelmaaseide/Desktop/USFinancialNewsArticles-preprocessed'
    data_directory = r"C:\Users\samba\OneDrive\Desktop\DS 4300 Large Scale Info\P01-verify-dataset"
    computer_chip = 'M2 Max'
    mem_size = 32

    # Index structures
    structures = index_all(data_directory)

    # If you want to call pickle, you can comment out the structures in index_all and load pickles here
    # pickles = ['/Users/michaelmaaseide/Desktop/avl_index.pkl','/Users/michaelmaaseide/Desktop/sortarr.pkl',
    #            '/Users/michaelmaaseide/Desktop/bst_index.pkl']
    # for pickle in pickles:
    #     structure = access_pickle(pickle)
    #     structures.append(structure)

    # Run experiments function on all indexed structures
    df, doclist = run_experiments(df, structures, data_directory, computer_chip, mem_size)

    # Save specific search result
    with open("search_results/doclist_for_AVL_searchset1=.txt", "w") as file:
        file.writelines(f"{item}\n" for item in doclist)

    # Save timing data
    df.to_csv('timing_data/timing_data.csv', index=False)

if __name__ == "__main__":
    main()