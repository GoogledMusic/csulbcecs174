# making a christmas tree with *s
tree_length = int(input("Enter the length of the tree: "))

for i in range (1, tree_length):
    print(" " * (tree_length - i) + "*" * (2 * i - 1))

print(" " * (tree_length - 1) + "*" * 2)