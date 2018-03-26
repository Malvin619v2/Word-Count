# Python program to find the k most frequent words
# from data set
from collections import Counter

data_set = "the quick brown fox jumps over the lazy brown dog, who thinks the world is flat and the skys blue. the brown fox then goes to sleep" \

# split() returns list of all the words in the string
split_it = data_set.split()

# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(3)

print(most_occur)
