import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

BSTnames = BSTNode(names_1[0])  # Start at first index in names_1
for name in range(1, len(names_1)):  # using range for list iteration through names
    # using BSTNode insert method, add each name to list for comparison
    BSTnames.insert(names_1[name])

for name2 in names_2:  # Now it's time to compare for dupes and print dupes to new list
    if BSTnames.contains(name2):
        duplicates.append(name2)

# Runtime for improved code is O(n) done twice over

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# runtime for original is O(n^2) - Quadratic

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
