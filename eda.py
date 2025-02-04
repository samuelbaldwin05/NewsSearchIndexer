import matplotlib.pyplot as plt
import pandas as pd

def graph_common_words(data, max_keys):
    # Count number of articles for each word
    counts = {key: len(value) for key, value in data}

    # Sort in descending order
    sorted_items = list(counts.items())
    sorted_items.sort(key=lambda item: item[1], reverse=True)

    # Just get the top few desired from max_keys
    top_items = sorted_items[:max_keys]

    # Get keys and values
    keys = [item[0] for item in top_items]
    values = [item[1] for item in top_items]

    # Plot
    plt.bar(keys, values)
    plt.xlabel('Words')
    plt.ylabel('Times Word Appears In Articles')
    plt.title('Most Common Words Across the Articles')
    plt.xticks(rotation=45)
    plt.show()

def graph_common_domains(data, max_keys):
    # Count number of articles for each word
    counts = {key: len(value) for key, value in data if "." in key}

    # Sort in descending order
    sorted_items = list(counts.items())
    sorted_items.sort(key=lambda item: item[1], reverse=True)

    # Just get the top few desired from max_keys
    top_items = sorted_items[:max_keys]

    # Get keys and values
    keys = [item[0] for item in top_items]
    values = [item[1] for item in top_items]

    # Plot
    plt.bar(keys, values)
    plt.xlabel('Articles')
    plt.ylabel('Frequency')
    plt.title('Most Common Domains')
    plt.xticks()
    plt.show()

def plot_search_time(df):
    """ Given search time dataframe, plot a line of
    """
    # Group by structure and search set size, getting mean search time
    avg_times = df.groupby(['index_type', 'search_set_base_size'])['search_time (ns)'].mean().reset_index()

    # Get all structures
    index_types = avg_times['index_type'].unique()

    # Plot
    plt.figure(figsize=(10, 6))
    for index_type in index_types:
        subset = avg_times[avg_times['index_type'] == index_type]
        plt.plot(subset['search_set_base_size'], subset['search_time (ns)'], marker='o', label=index_type)

    plt.xlabel('Search Set Base Size')
    plt.ylabel('Average Search Time (ns)')
    plt.title('Average Search Time vs. Search Set Base Size for Each Index Type')
    plt.legend(title='Index Type')
    plt.grid(True)
    plt.show()

def main():
    df = pd.read_csv(r"C:\Users\samba\OneDrive\Desktop\DS 4300 Large Scale Info\practical-01-fonsters\timing_data\timing_data.csv")
    df_no_linked_list = df[df["index_type"] != "Linked List"].copy()
    plot_search_time(df_no_linked_list)

if __name__ == "__main__":
    main()
# Graph Ideas
# Bar Graph of most common website urls
# Line chart of average time for each set of 5 experiments, line for each structure diff color (time vs n)