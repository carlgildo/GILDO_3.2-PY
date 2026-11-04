# Assessment 3.2: Linear Data Structure
**Last Name:** GILDO

## Contents
- `add_letters.py` — Algorithm 1: adds G, I, L, D, O one at a time.
- `remove_letters.py` — Algorithm 2: starts with G -> I -> L -> D -> O and removes O, D, L, I, G one at a time.

## Requirements from Assessment 3.2
- Edit/run the programs in PyCharm.
- Keep each program in its own Python file.
- Submit the program through a GitHub link.

## How to run in PyCharm
1. Extract this ZIP file.
2. Open the extracted `Assessment_3_2_GILDO` folder in PyCharm.
3. Open `add_letters.py` and click **Run**.
4. Open `remove_letters.py` and click **Run**.
5. To submit, create a GitHub repository and upload both `.py` files (you may also include this README).

## Data structure and order
The PDF for Assessment 3.1 shows the letters being added in this order:
G -> I -> L -> D -> O

It then shows removal in reverse order:
O, D, L, I, G

The Python list is used with `append()` to add at the end and `pop()` to remove from the end. This follows the last-in, first-out order demonstrated by the supplied algorithm.

## Expected output

### `add_letters.py`
Start: Empty (0 nodes)
- Add G: G (1 node)
- Add I: G -> I (2 nodes)
- Add L: G -> I -> L (3 nodes)
- Add D: G -> I -> L -> D (4 nodes)
- Add O: G -> I -> L -> D -> O (5 nodes)

### `remove_letters.py`
Starting structure: G -> I -> L -> D -> O (5 nodes)
- Remove O: G -> I -> L -> D (4 nodes)
- Remove D: G -> I -> L (3 nodes)
- Remove L: G -> I (2 nodes)
- Remove I: G (1 node)
- Remove G: Empty (0 nodes)
