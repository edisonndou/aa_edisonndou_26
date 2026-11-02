# task2/detyra1.py
# Implement remove(table, key) using a DELETED marker.

# Unique marker for deleted cells
# Equivalent to JavaScript Symbol('deleted')
DELETED = object()


# -----------------------------------------
# EXISTING TASK 1 FUNCTIONS
# -----------------------------------------

def num(key):
    if isinstance(key, (int, float)):
        return key

    s = 0
    for c in key:
        s += ord(c) - 64

    return s


def h(key, m):
    return num(key) % m


def chainedTable(keys, m):
    table = [[] for _ in range(m)]

    for key in keys:
        table[h(key, m)].append(key)

    return table


def probeInsert(table, key):
    m = len(table)
    i = h(key, m)

    for _ in range(m):
        if table[i] is None or table[i] is DELETED:
            table[i] = key
            return i

        i = (i + 1) % m

    raise OverflowError("Hash table is full")


def probeFind(table, key):
    m = len(table)
    i = h(key, m)

    for _ in range(m):
        if table[i] is None:
            return -1

        if table[i] is not DELETED and table[i] == key:
            return i

        i = (i + 1) % m

    return -1


def probeRemove(table, key):
    # Original Task 1 removal
    m = len(table)
    i = h(key, m)

    for _ in range(m):
        if table[i] is None:
            return -1

        if table[i] is not DELETED and table[i] == key:
            table[i] = None
            return i

        i = (i + 1) % m

    return -1


# -----------------------------------------
# TASK 2 - EXERCISE 1: REMOVE
# -----------------------------------------

def remove(table, key):
    """
    Remove a key by replacing it with DELETED.

    Requirements:
    - Search only along the key's probe path.
    - Do not change the table length.
    - Preserve searches behind deleted cells.
    - Return the removed index or -1.
    """
    m = len(table)
    i = h(key, m)

    for _ in range(m):
        if table[i] is None:
            return -1

        if table[i] is not DELETED and table[i] == key:
            table[i] = DELETED
            return i

        i = (i + 1) % m

    return -1


# -----------------------------------------
# TESTING
# -----------------------------------------

if __name__ == "__main__":

    W = [
        "A", "FOOL", "AND", "HIS",
        "MONEY", "ARE", "SOON", "PARTED"
    ]

    T = [None] * 13

    for word in W:
        probeInsert(T, word)

    print("TASK 2 - EXERCISE 1")
    print("Initial table:")

    for i, value in enumerate(T):
        print(i, value)

    print("\nResults:")

    result1 = remove(T, "ARE")
    result2 = probeFind(T, "SOON")
    result3 = probeFind(T, "ARE")
    result4 = remove(T, "KID")

    print("remove(T, 'ARE') =", result1)
    print("probeFind(T, 'SOON') =", result2)
    print("probeFind(T, 'ARE') =", result3)
    print("remove(T, 'KID') =", result4)

    print("\nFinal table:")

    for i, value in enumerate(T):
        if value is DELETED:
            value = "DELETED"
        print(i, value)

    assert result1 == 11
    assert result2 == 12
    assert result3 == -1
    assert result4 == -1
    assert len(T) == 13

    print("\nAll tests passed!")
