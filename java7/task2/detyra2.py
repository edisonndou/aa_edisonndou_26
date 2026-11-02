# task2/detyra2.py
# Double Hashing: Insertion and Searching

from detyra1 import num, h, DELETED


# -----------------------------------------
# DOUBLE HASH INSERT
# -----------------------------------------

def doubleHashInsert(table, key):
    """
    Insert a key using double hashing.

    First hash:
        i = h(key, m)

    Second hash:
        s = m - 2 - num(key) % (m - 2)

    On collision:
        i = (i + s) % m

    Returns the inserted index.
    """
    m = len(table)

    if m <= 2:
        raise ValueError("Table size must be greater than 2")

    i = h(key, m)
    s = m - 2 - num(key) % (m - 2)

    # Visit at most m cells
    for _ in range(m):

        # Empty or deleted cell can be reused
        if table[i] is None or table[i] is DELETED:
            table[i] = key
            return i

        # Collision: move using second hash
        i = (i + s) % m

    raise OverflowError("Hash table is full")


# -----------------------------------------
# DOUBLE HASH FIND
# -----------------------------------------

def doubleHashFind(table, key):
    """
    Search for a key using double hashing.

    Returns:
        Index if found
        -1 if not found

    DELETED cells are skipped.
    """
    m = len(table)

    if m <= 2:
        raise ValueError("Table size must be greater than 2")

    i = h(key, m)
    s = m - 2 - num(key) % (m - 2)

    # Search only along the key's probe path
    for _ in range(m):

        # None means the key is not present
        if table[i] is None:
            return -1

        # Found the requested key
        if table[i] is not DELETED and table[i] == key:
            return i

        # Move using the second hash
        i = (i + s) % m

    return -1


# -----------------------------------------
# DISPLAY HASH TABLE
# -----------------------------------------

def displayTable(table):
    """Display all hash table positions."""
    for i, value in enumerate(table):

        if value is DELETED:
            value = "DELETED"

        print(f"Index {i:2}: {value}")


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

if __name__ == "__main__":

    # Professor's example
    N = [30, 20, 56, 75, 31, 19]

    # Prime-sized table
    D = [None] * 11

    print("=" * 55)
    print("TASK 2 - EXERCISE 2: DOUBLE HASHING")
    print("=" * 55)

    # Insert all numbers
    print("\nINSERTION PROCESS")

    for key in N:
        index = doubleHashInsert(D, key)

        print(
            f"Inserted {key} at index {index}"
        )

    # Display final table
    print("\nFINAL HASH TABLE")
    displayTable(D)

    # Search tests
    print("\nSEARCH RESULTS")

    result1 = doubleHashFind(D, 19)
    result2 = doubleHashFind(D, 42)

    print("doubleHashFind(D, 19) =", result1)
    print("doubleHashFind(D, 42) =", result2)

    # Expected results from professor's slide
    expected_table = [
        None, 56, None, 31, 75, 19,
        None, None, 30, 20, None
    ]

    # Verify the table and search results
    assert D == expected_table
    assert result1 == 5
    assert result2 == -1

    print("\nSUCCESS: ALL TESTS PASSED!")
