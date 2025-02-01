import json
import pickle
import re

from streamlit.elements.lib.options_selector_utils import index_

from indexer.sortedarr.sortedarray import SortedArray
from indexer.linkedlist.linklist import LinkedList
from indexer.maps.hash_map import HashMapIndex
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.util.timer import timer
from indexer.abstract_index import AbstractIndex
from pathlib import Path

from tests.test_ll import linked_list


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
    domain = url.split("/")
    # Items after second /  (www.site.com)
    domain = domain[2].split(".")
    # Split after . www, site, com, then join site and com
    if len(domain) > 2:
        return domain[1] + "." + domain[2]
    else:
        return domain[0] + "." + domain[1]


@timer
def index_files(path: str, index: AbstractIndex) -> None:
    path = Path(path)

    if path is not None:
        print(f"path = {path}")

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
    data_directory = r"C:\Users\samba\OneDrive\Desktop\DS 4300 Large Scale Info\USFinancialNewsArticles-preprocessed"
    # data_directory = r"C:\Users\samba\OneDrive\Desktop\DS 4300 Large Scale Info\P01-verify-dataset"
    # Michaels directory
    # data_directory = '/Users/michaelmaaseide/Desktop/P01-verify-dataset'

    # Sorted Array
    # sortarr_index = SortedArray()
    # index_files(data_directory, sortarr_index)
    # search = "act"
    # print(sortarr_index.search(search))
    # print(sortarr_index.result())

    # BST test
    # bst_index = BinarySearchTreeIndex()
    # index_files(data_directory, bst_index)
    # print(bst_index.get_keys_in_order())
    # search_word = 'act'
    # search_results = bst_index.search(search_word)
    # print(f"Files with {search_word}: {search_results}")
    # print(bst_index.get_keys_in_order())

    # Linked List
    # ll_index = LinkedList()
    # index_files(data_directory, ll_index)
    # save_pickle(ll_index, "llindex.pkl")

    # AVL Tree
    # avl_index = AVLTreeIndex()
    # index_files(data_directory, avl_index)
    # keys = avl_index.get_keys()
    # print(len(keys))
    # print("Height:", avl_index._height(avl_index.root))
    # search = 'act'
    # search_results = avl_index.search(search)
    # print(f"Files with {search}: {search_results}")
    # save_pickle(avl_index, "avlindex.pkl")
    # loaded_index = access_pickle("avl_index.pkl")
    # print(loaded_index.get_keys())

    # Hash Map
    hash_index = HashMapIndex(250049)
    index_files(data_directory, hash_index)
    search = 'act'
    search_results = hash_index.search(search)
    print(f"Files with {search}: {search_results}")

if __name__ == "__main__":
    main()
