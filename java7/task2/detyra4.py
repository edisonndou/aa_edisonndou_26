# task2/detyra4.py
# Dynamic Hash Table Growth
# Function: insertGrow(table, key)

from detyra1 import (
    DELETED,
    probeInsert,
    probeFind
)


# -----------------------------------------
# CHECK IF A NUMBER IS PRIME
# -----------------------------------------

def isPrime(n):
    """
    Return True if n is a prime number.
    Otherwise return False.
    """
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True


# -----------------------------------------
# FIND THE NEXT PRIME NUMBER
# -----------------------------------------

def nextPrime(n):
    """
    Return the smallest prime number
    greater than or equal to n.
    """
    while not isPrime(n):
        n += 1

    return n


# -----------------------------------------
# TASK 2 - EXERCISE 4: INSERT GROW
# -----------------------------------------

def insertGrow(table, key):
    """
    Insert a key while keeping the load
    factor at 0.5 or below.

    Steps:
    1. Count active keys.
    2. Ignore None and DELETED cells.
    3. Check if insertion exceeds 0.5.
    4. If needed, grow to nextPrime(2*m).
    5. Reinsert old keys in index order.
    6. Insert the new key.
    7. Return the resulting table.
    """

    m = len(table)

    if m == 0:
        raise ValueError("Table must not be empty")

    # Step 1: Count active keys
    n = 0

    for value in table:
        if value is not None and value is not DELETED:
            n += 1

    # Step 2: Calculate load factor
    new_load_factor = (n + 1) / m

    # Step 3: Grow when necessary
    if new_load_factor > 0.5:

        # Calculate new prime table size
        new_size = nextPrime(2 * m)

        # Create new empty table
        new_table = [None] * new_size

        # Reinsert old keys in index order
        for value in table:

            if value is None or value is DELETED:
                continue

            probeInsert(new_table, value)

        # Replace old table reference
        table = new_table

    # Step 4: Insert new key
    probeInsert(table, key)

    # Step 5: Return the table
    return table


# -----------------------------------------
# DISPLAY HASH TABLE
# -----------------------------------------

def displayTable(table):
    """Display hash table contents."""
    for i, value in enumerate(table):

        if value is DELETED:
            value = "DELETED"

        print(f"Index {i:2}: {value}")


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

if __name__ == "__main__":

    # Professor's word example
    W = [
        "A", "FOOL", "AND", "HIS",
        "MONEY", "ARE", "SOON", "PARTED"
    ]

    # Initial table size = 5
    G = [None] * 5

    print("=" * 60)
    print("TASK 2 - EXERCISE 4: INSERT GROW")
    print("=" * 60)

    print("\nINITIAL TABLE SIZE:", len(G))

    # Track table sizes
    sizes = [len(G)]

    # Insert all words
    for word in W:

        old_size = len(G)

        G = insertGrow(G, word)

        new_size = len(G)

        sizes.append(new_size)

        print(
            f"Inserted {word:<8} "
            f"| Old size: {old_size:<3} "
            f"| New size: {new_size}"
        )

    # -------------------------------------
    # FINAL TABLE
    # -------------------------------------

    print("\nFINAL HASH TABLE")
    displayTable(G)

    # -------------------------------------
    # PROFESSOR'S CHECKS
    # -------------------------------------

    print("\nEXPECTED TABLE SIZES:")
    print([5, 5, 5, 11, 11, 11, 23, 23, 23])

    print("\nACTUAL TABLE SIZES:")
    print(sizes)

    print("\nFINAL TABLE LENGTH:")
    print("G.length =", len(G))

    print("\nSEARCH FOR ARE:")
    are_index = probeFind(G, "ARE")

    print("probeFind(G, 'ARE') =", are_index)

    # -------------------------------------
    # ASSERTIONS
    # -------------------------------------

    expected_sizes = [
        5, 5, 5, 11, 11, 11, 23, 23, 23
    ]

    assert sizes == expected_sizes, (
        f"Incorrect table sizes: {sizes}"
    )

    assert len(G) == 23, (
        f"Expected size 23, got {len(G)}"
    )

    assert are_index == 4, (
        f"Expected ARE at index 4, got {are_index}"
    )

    # Check final load factor
    active_keys = sum(
        1 for value in G
        if value is not None and value is not DELETED
    )

    load_factor = active_keys / len(G)

    assert load_factor <= 0.5

    print("\nFINAL LOAD FACTOR:")
    print(f"{load_factor:.4f}")

    print("\nSUCCESS: ALL TESTS PASSED!")
