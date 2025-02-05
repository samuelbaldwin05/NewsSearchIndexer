## DS 4300 Index Builder

### Executing the program

The easiest way to run the function is to go to experiments.py, change the data_directory variable to the location of the folder,
and run the file. Additionally, the computer chip and the memory size can also be changed to the specs of the computer
it is being run on. (Note: If the experiments are being run on a smaller folder, the length list of the size of the search
sets should be modified accordingly, ex: length_lst = [4, 8, 12, 16, 20, 24, 28, 32] ) 

However, this is not how we did it. Due to not wanting to rerun the indexer, we pickled the AVL, BST, 
and Sorted Array in the assign_01.py file, which is also where some statistics were gathered and some graphs were 
created. We then called accessed the files we did pickle in the experiments.py and then indexed the ones we had not
pickled. 

After inputting the data directory, assign_01.py has the function index_files, which is called to index the file
for each of the structures we created. The results of the indexed structures are then appended to the 'structures' list
which is input into the run_experiments function in the experiments.py. run_experiments seperates the structures and 
the length of the number of search terms wanted, creates a search set for each length, and tests each structure 5 times 
on each search set. This is timed, and the data is returned and saved into the timing_data folder in the file timing_data.csv.
Additionally, experiments.py also returns the search set from the first test, which is in written into the search_results
folder.