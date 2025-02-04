import json
import pickle
import re
from os import access
from pathlib import Path
from typing import Optional

from indexer.abstract_index import AbstractIndex
from eda import graph_common_words, graph_common_domains
# Structure imports
from indexer.sortedarr.sortedarray import SortedArray
from indexer.linkedlist.linklist import LinkedList
from indexer.maps.hash_map import HashMapIndex
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.trees.bst_index import BinarySearchTreeIndex



def process_titles(title):
    """ Given a title, process the title, splitting words into spaces, removing punctuation"""
    title_cleaned = re.sub(r"[^A-Za-z\s]", "", title)
    title_cleaned = title_cleaned.lower()
    title_words = title_cleaned.split(" ")
    return [title for title in title_words if len(title) > 0]

def last_name(author_name):
    """ Given an authors name, return their last name"""
    author_name = author_name.lower()
    names = author_name.split(" ")
    return names[-1]

def domain_name(url):
    """Given a url return the domain name"""
    url = url.lower()
    domain = url.split("/")
    # Items after second /  (www.site.com)
    domain = domain[2].split(".")
    # Split after . www, site, com, then join site and com
    if len(domain) > 2:
        return domain[1] + "." + domain[2]
    else:
        return domain[0] + "." + domain[1]

def index_files(path: str, index: AbstractIndex, count: Optional[int] = None) -> None:
    """ Given a folder path and a structure index, read in the preprocessed words, author name, url, and title,
    preprocessing the author name to get last name, url to get domain, and title to break into words. Insert each
    of the preprocessed items into the given structure. Additionally, if a count is given, only iterate through
    the desired number of files"""
    path = Path(path)

    if path is not None:
        print(f"path = {path}")
    counter = 0
    for file in path.rglob("*.json"):
        # Load data
        file_data = json.loads(file.read_text(encoding="utf-8"))

        # Get preprocessed text and filename
        words = file_data["preprocessed_text"]
        file_name = file.name

        # Index author last name 
        author_last_name = last_name(file_data["author"])
        if len(author_last_name) != 0:
            index.insert(author_last_name, file_name)

        # Index url
        url = file_data["url"]
        if len(url) != 0:
            domain = domain_name(url)
            index.insert(domain, file_name)

        # Include list of preprocessed title words in words to be indexed
        title_words = process_titles(file_data["title"])
        if len(title_words) != 0:
            for title_word in title_words:
                if len(title_word) != 0:
                    index.insert(title_word, file_name)

        # Insert
        for word in words:
            index.insert(word, file_name)

        # Counter for only indexing a given number of files
        counter += 1
        if counter == count and count is not None:
            break

def save_pickle(index, file_name):
    """ Given indexed key values and a desired file name, pickle the info for easy access later"""
    with open(file_name, "wb") as file:
        pickle.dump(index, file)

def access_pickle(file_name):
    """" Access previously pickled info using given file name"""
    with open(file_name, "rb") as file:
        return pickle.load(file)

def main():
    # Directories
    # Sams directory
    data_directory = r"C:\Users\samba\OneDrive\Desktop\DS 4300 Large Scale Info\avl_index.pkl"
    data_directory1 = r"C:\Users\samba\OneDrive\Desktop\DS 4300 Large Scale Info\P01-verify-dataset"
    # Michaels directory
    # data_directory = '/Users/michaelmaaseide/Desktop/hashindex.pkl'

    ### PICKLING

    # BST
    #bst_index = BinarySearchTreeIndex()
    # index_files(data_directory, bst_index)
    # save_pickle(bst_index, 'bst.pkl')
    # bst_index = access_pickle(bst_pickle)
    # search_word = 'act'
    # search_results = bst_index.search(search_word)
    # print(f"Files with {search_word}: {search_results}")

    # Create EDA graphs
    # bst_index = access_pickle(data_directory)
    # data = bst_index.get_keyvalues_in_order()
    # Common words
    # graph_common_words(data, 10)
    # Common domains
    # graph_common_domains(data, 5)

    # Get Stats
    #bst_index = BinarySearchTreeIndex()
    #index_files(data_directory1, bst_index)
    # bst_index = access_pickle(data_directory)
    # print("Files:", bst_index.get_unique_values()) # Num Files
    # print("Height:", bst_index.tree_height())
    # print("Num words", bst_index.count_nodes())  # Num words
    # print("Num words", len(bst_index.get_keys()))

    # AVL Tree
    # avl_index = AVLTreeIndex()
    # index_files(data_directory, avl_index)
    # save_pickle(avl_index, "avlindex.pkl")
    # search = 'act'
    # search_results = avl_index.search(search)
    # print(f"Files with {search}: {search_results}")

    # Stats
    # avl_index = access_pickle(data_directory)
    # print(avl_index.get_unique_values())
    # print(len(avl_index.get_keys()))
    # print(avl_index._height(avl_index.root))

    # Linked List
    # ll_index = LinkedList()
    # index_files(data_directory, ll_index)
    # save_pickle(ll_index, "llindex.pkl")
    # search_results = ll_index.search(search_word)
    # print(f"Files with {search_word}: {search_results}")

    # Sorted Array
    # sortarr_index = SortedArray()
    # index_files(data_directory, sortarr_index)
    # save_pickle(sortarr_index, "sortarr.pkl")
    # search_word = "act"
    # search_results = sortarr_index.search(search_word)
    # print(f"Files with {search_word}: {search_results}")

    # Hash Map
    # hash_index = HashMapIndex(250049)
    # index_files(data_directory, hash_index)
    # print(hash_index.get_unique_values())
    # search = 'act'
    # search_results = hash_index.search(search)
    # print(f"Files with {search}: {search_results}")

if __name__ == "__main__":
    main()
