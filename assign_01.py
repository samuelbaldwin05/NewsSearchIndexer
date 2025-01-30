import json
import pickle
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.util.timer import timer
from indexer.abstract_index import AbstractIndex
from pathlib import Path

@timer
def index_files(path: str, index: AbstractIndex) -> None:
    path = Path(path)

    if path is not None:
        print(f"Starting to index files in {path}")

    # Go through all subfolders
    for file in path.rglob("*.json"):
        if file.is_file():
            file_data = json.loads(file.read_text(encoding="utf-8"))
            words = file_data["preprocessed_text"]
            file_name = file.name
            for word in words:
                index.insert(word, file_name)

# @timer
# def index_words(path: str, index: AbstractIndex) -> None:
#     path = Path(path)
#
#     if path is not None:
#         print(f"path = {path}")
#
#     for file in path.glob("*.json"):
#         file_data = json.loads(file.read_text(encoding="utf-8"))
#         words = file_data["preprocessed_text"]
#         file_name = file.name
#         for word in words:
#             index.insert(file_name, words)

# # A simple demo of how the @timer decoration can be used
# @timer
# def loopy_loop():
#     total = sum((x for x in range(0, 1000000)))

def save_pickle(index, file_name):
    """ Given indexed key values and a desired file name, pickle the info for easy access later"""
    with open(file_name, "wb") as file:
        pickle.dump(index, file)

def access_pickle(file_name):
    """" Access previously pickled info using given file name"""
    with open(file_name, "rb") as file:
        return pickle.load(file)

def main():
    # You'll need to change this to be the absolute path to the root folder
    # of the dataset
    # Sams directory
    # data_directory = r"C:\Users\samba\OneDrive\Desktop\DS 4300 Large Scale Info\USFinancialNewsArticles-preprocessed\April2018"
    # data_directory = r"C:\Users\samba\OneDrive\Desktop\DS 4300 Large Scale Info\P01-verify-dataset"
    data_directory = r"/Users/jeffreykrapf/Desktop/ds4300/USFinancialNewsArticles-preprocessed"

    # Here, we are creating a sample binary search tree index object
    # and sending it to the index_files function
    # bst_index = BinarySearchTreeIndex()
    # index_files(data_directory, bst_index)
    #
    # # As a gut check, we are printing the keys that were added to the
    # # index in order.
    # print(bst_index.get_keys_in_order())
    #
    # search_word = 'act'
    # search_results = bst_index.search(search_word)
    # print(f"Files with {search_word}: {search_results}")


    # AVL Tree tests
    avl_index = AVLTreeIndex()
    #index_words(data_directory, avl_index)
    index_files(data_directory, avl_index)
    keys = avl_index.get_keys()
    print(len(keys))
    # print(keys)
    print("Height:", avl_index._height(avl_index.root))

    #search = 'preproc-news_0001728.json'
    # search = 'act'
    # search_results = avl_index.search(search)
    # print(f"Files with {search}: {search_results}")
    save_pickle(avl_index, "avlindex.pkl")
    #loaded_index = access_pickle("avl_index.pkl")
    #print(loaded_index.get_keys())
    # quick demo of how to use the timing decorator included
    # in indexer.util
    # loopy_loop()



if __name__ == "__main__":
    main()
