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

def generate_unique_id():
    return str(uuid.uuid4())


@timer
def experiment(df, structure, search, com_type, mem_size, index_type, n):

    num_tokens = len(search)
    uniqueid = generate_unique_id()
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
        "search_time": 00
    }

    df = df.append(new_row, ignore_index=True)


def access_pickle(file_name):
    """" Access previously pickled info using given file name"""
    with open(file_name, "rb") as file:
        return pickle.load(file)


def main():

    columns = [
        "run_id",
        "compute_proc_type",
        "primary_memory_size",
        "index_type",
        "num_docs_indexed",
        "num_tokens_indexed",
        "search_set_base_size",
        "search_time"
    ]


    df = pd.DataFrame(columns=columns)
    pickle_data = '/Users/michaelmaaseide/Desktop/avl_index.pkl'
    avl = access_pickle(pickle_data)

    length_lst = [4000,5000,6000,7000,8000,9000,10000,11000]
    sets = generate_search_set(length_lst, pickle_data)

    experiment(df, avl, sets[0], 'M2 Max', 32, 'AVL', length_lst[0])
    print(df)



if __name__ == "__main__":
    main()