"""
Assessment 3.2 - Linear Data Structure
Algorithm 2: Remove each letter until the structure becomes empty.

The program begins with the completed structure from Algorithm 1:
G -> I -> L -> D -> O.
It removes from the end, in the exact order shown in Assessment 3.1:
O, D, L, I, G.
"""

linear_data = list("GILDO")

print("ASSESSMENT 3.2: LINEAR DATA STRUCTURE")
print("ALGORITHM 2: REMOVE EACH LETTER UNTIL EMPTY")
print("\nStarting structure:", " -> ".join(linear_data))
print("Starting nodes:", len(linear_data))

while linear_data:
    removed_letter = linear_data.pop()
    if linear_data:
        structure = " -> ".join(linear_data)
    else:
        structure = "Empty"

    print(
        f"Remove {removed_letter}: {structure} "
        f"({len(linear_data)} nodes)"
    )

print("\nEnd: Empty (0 nodes)")
