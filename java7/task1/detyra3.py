
# detyra3.py
# TASK 3: Removing a Key (Professor's Algorithm)

from detyra1 import h
from detyra2 import probeInsert, probeFind


def probeRemove(table, key):
    """
    Remove a key using linear probing.
    The matching cell is set to None.
    Returns the removed index or -1.
    """
    m = len(table)
    i = h(key, m)
    start = i

    while table[i] is not None:
        if table[i] == key:
            table[i] = None
            return i

        i = (i + 1) % m

        if i == start:
            return -1

    return -1


if __name__ == "__main__":
    W = [
        "A", "FOOL", "AND", "HIS",
        "MONEY", "ARE", "SOON", "PARTED"
    ]

    T = [None] * 13

    for word in W:
        probeInsert(T, word)

    print("TASK 3: PROBE REMOVE")

    print("\nBefore removal:")
    for i, value in enumerate(T):
        print(f"Index {i}: {value}")

    removed_index = probeRemove(T, "ARE")

    print("\nRemoved ARE from index:", removed_index)

    print("\nAfter removal:")
    for i, value in enumerate(T):
        print(f"Index {i}: {value}")

    print("\nFind SOON:", probeFind(T, "SOON"))
    print("Find ARE:", probeFind(T, "ARE"))
