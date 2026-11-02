
# detyra1.py
# TASK 1: Open Hashing (Separate Chaining)

def num(key):
    """
    Convert a key into a numeric value.
    A=1, B=2, ..., Z=26.
    """
    if isinstance(key, (int, float)):
        return key

    s = 0
    for c in key:
        s += ord(c) - 64

    return s


def h(key, m):
    """Calculate the hash index."""
    return num(key) % m


def chainedTable(keys, m):
    """Create a hash table using separate chaining."""
    table = []

    for i in range(m):
        table.append([])

    for k in keys:
        table[h(k, m)].append(k)

    return table


if __name__ == "__main__":
    W = [
        "A", "FOOL", "AND", "HIS",
        "MONEY", "ARE", "SOON", "PARTED"
    ]

    table = chainedTable(W, 13)

    print("TASK 1: OPEN HASHING")

    for i, values in enumerate(table):
        print(f"Index {i}: {values}")

    print("\nchainedTable(W, 13)[11]:")
    print(table[11])
