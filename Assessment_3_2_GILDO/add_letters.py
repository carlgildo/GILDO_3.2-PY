"""
Assessment 3.2 - Linear Data Structure
Algorithm 1: Add each letter of the surname GILDO.

This program uses a Python list as a stack-like linear data structure.
It adds the letters in the exact order shown in Assessment 3.1:
G, I, L, D, O.
"""

surname = "GILDO"
linear_data = []

print("ASSESSMENT 3.2: LINEAR DATA STRUCTURE")
print("ALGORITHM 1: ADD EACH LETTER OF GILDO")
print("\nStart: Empty (0 nodes)")

for letter in surname:
    linear_data.append(letter)
    print(
        f"Add {letter}: {' -> '.join(linear_data)} "
        f"({len(linear_data)} nodes)"
    )

print("\nFinal structure:", " -> ".join(linear_data))
print("Total nodes:", len(linear_data))
