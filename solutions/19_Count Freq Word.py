def word_frequency(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
    #     if word in freq:
    #         freq[word] += 1
    #     else:
    #         freq[word] = 1
    # return freq


# Example usage
words = ["orange","apple", "banana", "apple", "orange", "banana", "apple"]
print(word_frequency(words))

#shortcut using counter
from collections import Counter
def word_frequency_counter(words):
    #convert counter object to dictionary
    return dict(Counter(words))

print(word_frequency_counter(words))

# Sort by frequency and return top k
def sort_by_frequency(freq_dict, k):
    return dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)[:k])

print(sort_by_frequency(word_frequency(words), 2))