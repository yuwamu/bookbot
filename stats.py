def get_num_words(text):
    return len(text.split())

def get_character_count(text):
    counts = {}

    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts

# Replacement for lambda: define a separate function for the sort key
def get_count(item):
    return item['count']


def sorted_counts(counts_dict):
    counts_list = [{'char': char, 'count': count} for char, count in counts_dict.items()]
    return sorted(counts_list, key=get_count)
