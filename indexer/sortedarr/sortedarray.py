class Node:
    def __init__(self, term):
        """Node in the sorted array which uses the term as a key and list """
        self.values = []
        self.term = term


    def add_file(self, filename):
        """Adds file to node list of values"""
        self.values.append(filename)

class SortedArray:
    def __init__(self):
        self.keys = []

    def binary_search(self, term):
        """ utilizes binary search to find the sorted index where the node should be inserted
            returns the index where the term should be inserted and a boolean if the term should
            be appended due to an already existing node"""
        start, end = 0, len(self.keys) - 1
        while start <= end:
            middle = start + (end - start) // 2
            if self.keys[middle].term == term: # will only get to this point if term already exists
                return middle, True # if the middle is the term then we have found our already existing term
            if self.keys[middle].term < term: # middle term is less than our term parameter
                start = middle + 1 # setting left bound index to middle + 1
            if self.keys[middle].term > term: # middle term is greater than our term parameter
                end = middle - 1 # setting right bound index to middle - 1
        return start, False

    def insert(self, term, filename):
        """ Inserts term nodes into sorted array data structure, ensures it stays sorted by
            dynamically inserting nodes in a sorted manner"""
        index, exists = self.binary_search(term)
        if exists:
            self.keys[index].add_file(filename)
        else:
            new_node = Node(term)
            new_node.add_file(filename)
            self.keys.insert(index, new_node)

    def search(self, term):
        """ Searches for a term"""
        index, exists = self.binary_search(term)
        if exists:
            return self.keys[index].values
        else:
            return []

    def result(self):
        """ Displays entire sorted array"""
        return [(node.term, node.values) for node in self.keys]