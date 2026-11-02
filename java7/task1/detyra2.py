
# detyra2.py
# TASK 2: Closed Hashing (Linear Probing)

from detyra1 import h


def probeInsert(table, key):
    """
    Insert a key using linear probing.
    Returns the inserted index.
    """
    m = len(table)
    i = h(key, m)
    start = i

    while table[i] is not None:
        i = (i + 1) % m

        if i == start:
            raise OverflowError("Hash table is full")

    table[i] = key
    return i


def probeFind(table, key):
    """
    Search for a key using linear probing.
    Returns the index or -1 if not found.
    """
    m = len(table)
    i = h(key, m)
    start = i

    while table[i] is not None:
        if table[i] == key:
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
        index = probeInsert(T, word)
        print(f"Inserted {word} at index {index}")

    print("\nTASK 2: CLOSED HASHING")

    for i, value in enumerate(T):
        print(f"Index {i}: {value}")

    print("\nSearch results:")
    print("PARTED:", probeFind(T, "PARTED"))
    print("KID:", probeFind(T, "KID"))
