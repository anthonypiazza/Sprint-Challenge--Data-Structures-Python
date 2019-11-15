import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# name_2 = []
# for name_1 in names_2:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# RUNTIME IN BIG O NOTATION IS O(n^2) - nested for loops

bst = BinarySearchTree(names_1[0])

for i in range(1, len(names_1)-1):
    current_name = names_1[i]
    bst.insert(current_name)

for i in range(0, len(names_2)-1):
    current_name = names_2[i]
    if bst.contains(current_name):
        duplicates.append(current_name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

