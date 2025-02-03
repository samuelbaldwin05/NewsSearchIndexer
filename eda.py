import matplotlib.pyplot as plt

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