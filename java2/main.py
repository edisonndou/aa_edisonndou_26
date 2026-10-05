# Krahasim i kompleksitetit iterativ dhe rekursiv me funksione jo elementare.

def bashko(numrat: list[int], fillimi: int, mesi: int, fundi: int, ndihmese: list[int]) -> None:
    majtas = fillimi
    djathtas = mesi
    pozita = fillimi

    while majtas < mesi and djathtas < fundi:
        if numrat[majtas] <= numrat[djathtas]:
            ndihmese[pozita] = numrat[majtas]
            majtas += 1
        else:
            ndihmese[pozita] = numrat[djathtas]
            djathtas += 1

        pozita += 1

    while majtas < mesi:
        ndihmese[pozita] = numrat[majtas]
        majtas += 1
        pozita += 1

    while djathtas < fundi:
        ndihmese[pozita] = numrat[djathtas]
        djathtas += 1
        pozita += 1

    numrat[fillimi:fundi] = ndihmese[fillimi:fundi]


def merge_sort_rekursiv(numrat: list[int]) -> list[int]:
    rezultati = numrat[:]
    ndihmese = [0] * len(rezultati)

    def rendit(fillimi: int, fundi: int) -> None:
        if fundi - fillimi <= 1:
            return

        mesi = (fillimi + fundi) // 2
        rendit(fillimi, mesi)
        rendit(mesi, fundi)
        bashko(rezultati, fillimi, mesi, fundi, ndihmese)

    rendit(0, len(rezultati))

    return rezultati


def merge_sort_iterativ(numrat: list[int]) -> list[int]:
    rezultati = numrat[:]
    ndihmese = [0] * len(rezultati)
    gjeresia = 1

    while gjeresia < len(rezultati):
        for fillimi in range(0, len(rezultati), 2 * gjeresia):
            mesi = min(fillimi + gjeresia, len(rezultati))
            fundi = min(fillimi + 2 * gjeresia, len(rezultati))
            bashko(rezultati, fillimi, mesi, fundi, ndihmese)

        gjeresia *= 2

    return rezultati


def fuqia_binare_iterative(baza: int, eksponenti: int) -> int:
    if eksponenti < 0:
        raise ValueError("Eksponenti duhet të jetë numër jo negativ.")

    rezultati = 1
    faktori = baza
    fuqia = eksponenti

    while fuqia > 0:
        if fuqia % 2 == 1:
            rezultati *= faktori

        faktori *= faktori
        fuqia //= 2

    return rezultati


def fuqia_binare_rekursive(baza: int, eksponenti: int) -> int:
    if eksponenti < 0:
        raise ValueError("Eksponenti duhet të jetë numër jo negativ.")

    if eksponenti == 0:
        return 1

    gjysma = fuqia_binare_rekursive(baza, eksponenti // 2)

    if eksponenti % 2 == 0:
        return gjysma * gjysma

    return baza * gjysma * gjysma


def shpjego_merge_sort(numrat: list[int]) -> None:
    print("1. Merge Sort - kompleksitetet mbeten të njëjta")
    print("Inputi:", numrat)
    print("Rezultati iterativ:", merge_sort_iterativ(numrat))
    print("Rezultati rekursiv:", merge_sort_rekursiv(numrat))
    print("Iterativ:  kohë O(n log n), hapësirë O(n)")
    print("Rekursiv: kohë O(n log n), hapësirë O(n)")
    print("Pse?")
    print("- Të dy variantet kryejnë log n nivele bashkimi.")
    print("- Në çdo nivel përpunohen të n elementet.")
    print("- Të dy përdorin një varg ndihmës me n elemente.")
    print("- Stack-u rekursiv O(log n) nuk e ndryshon O(n) total.")


def shpjego_fuqine_binare(baza: int, eksponenti: int) -> None:
    print("\n2. Fuqizimi binar - rekursioni degradon hapësirën")
    print(f"Inputi: {baza}^{eksponenti}")
    print("Rezultati iterativ:", fuqia_binare_iterative(baza, eksponenti))
    print("Rezultati rekursiv:", fuqia_binare_rekursive(baza, eksponenti))
    print("Iterativ:  kohë O(log n), hapësirë O(1)")
    print("Rekursiv: kohë O(log n), hapësirë O(log n)")
    print("Pse?")
    print("- Në çdo hap eksponenti përgjysmohet, ndaj koha është O(log n).")
    print("- Varianti iterativ ruan vetëm disa ndryshore, pra O(1).")
    print("- Varianti rekursiv mban një thirrje për çdo përgjysmim në stack,")
    print("  prandaj hapësira degradohet në O(log n).")


def dfs_iterativ(grafi: dict[str, list[str]], fillimi: str) -> list[str]:
    if fillimi not in grafi:
        raise ValueError("Nyja fillestare nuk ekziston ne graf.")

    vizituar = set()
    renditja = []
    steku = [fillimi]

    while steku:
        nyja = steku.pop()

        if nyja in vizituar:
            continue

        vizituar.add(nyja)
        renditja.append(nyja)

        for fqinji in reversed(grafi[nyja]):
            if fqinji not in grafi:
                raise ValueError(f"Nyja {fqinji} nuk ka liste fqinjesh.")

            if fqinji not in vizituar:
                steku.append(fqinji)

    return renditja


def dfs_rekursiv(grafi: dict[str, list[str]], fillimi: str) -> list[str]:
    if fillimi not in grafi:
        raise ValueError("Nyja fillestare nuk ekziston ne graf.")

    vizituar = set()
    renditja = []

    def vizito(nyja: str) -> None:
        vizituar.add(nyja)
        renditja.append(nyja)

        for fqinji in grafi[nyja]:
            if fqinji not in grafi:
                raise ValueError(f"Nyja {fqinji} nuk ka liste fqinjesh.")

            if fqinji not in vizituar:
                vizito(fqinji)

    vizito(fillimi)

    return renditja


def shpjego_dfs(grafi: dict[str, list[str]], fillimi: str) -> None:
    print("\n3. DFS ne graf - kompleksitetet mbeten te njejta")
    print("Grafi:", grafi)
    print("Nyja fillestare:", fillimi)
    print("Rezultati iterativ:", dfs_iterativ(grafi, fillimi))
    print("Rezultati rekursiv:", dfs_rekursiv(grafi, fillimi))
    print("Iterativ:  kohe O(V + E), hapesire O(V)")
    print("Rekursiv: kohe O(V + E), hapesire O(V)")
    print("Pse?")
    print("- Secila nyje vizitohet nje here dhe secila lidhje kontrollohet nje here.")
    print("- Varianti iterativ mund te ruaje deri ne V nyje ne stek.")
    print("- Varianti rekursiv mund te kete deri ne V thirrje ne call stack.")
    print("- Nyjet e vizituara kerkojne O(V) hapesire ne te dy variantet.")


def kostoja_e_zinxhirit_dinamike(dimensionet: list[int]) -> int:
    if len(dimensionet) < 2 or any(dimension <= 0 for dimension in dimensionet):
        raise ValueError("Dimensionet duhet te permbajne te pakten dy vlera pozitive.")

    numri_i_matricave = len(dimensionet) - 1
    kostot = [[0] * numri_i_matricave for _ in range(numri_i_matricave)]

    for gjatesia in range(2, numri_i_matricave + 1):
        for fillimi in range(numri_i_matricave - gjatesia + 1):
            fundi = fillimi + gjatesia - 1
            kostot[fillimi][fundi] = float("inf")

            for ndarja in range(fillimi, fundi):
                kostoja = (
                    kostot[fillimi][ndarja]
                    + kostot[ndarja + 1][fundi]
                    + dimensionet[fillimi]
                    * dimensionet[ndarja + 1]
                    * dimensionet[fundi + 1]
                )
                kostot[fillimi][fundi] = min(kostot[fillimi][fundi], kostoja)

    return kostot[0][numri_i_matricave - 1]


def kostoja_e_zinxhirit_rekursive(dimensionet: list[int]) -> int:
    if len(dimensionet) < 2 or any(dimension <= 0 for dimension in dimensionet):
        raise ValueError("Dimensionet duhet te permbajne te pakten dy vlera pozitive.")

    def llogarit(fillimi: int, fundi: int) -> int:
        if fillimi == fundi:
            return 0

        kostoja_minimale = float("inf")

        for ndarja in range(fillimi, fundi):
            kostoja = (
                llogarit(fillimi, ndarja)
                + llogarit(ndarja + 1, fundi)
                + dimensionet[fillimi]
                * dimensionet[ndarja + 1]
                * dimensionet[fundi + 1]
            )
            kostoja_minimale = min(kostoja_minimale, kostoja)

        return kostoja_minimale

    return llogarit(0, len(dimensionet) - 2)


def shpjego_zinxhirin_e_matricave(dimensionet: list[int]) -> None:
    print("\n4. Matrix Chain Multiplication - rekursioni degradon kohen")
    print("Dimensionet:", dimensionet)
    print("Kostoja minimale dinamike:", kostoja_e_zinxhirit_dinamike(dimensionet))
    print("Kostoja minimale rekursive:", kostoja_e_zinxhirit_rekursive(dimensionet))
    print("Dinamik:  kohe O(n^3), hapesire O(n^2)")
    print("Rekursiv: kohe O(3^n), hapesire O(n)")
    print("Pse?")
    print("- Programimi dinamik e llogarit secilin nenproblem vetem nje here.")
    print("- Rekursioni naiv provon cdo ndarje dhe rillogarit nenproblemet.")
    print("- Numri i thirrjeve rritet eksponencialisht, ndaj koha degradohet.")


def main() -> None:
    numrat = [38, 27, 43, 3, 9, 82, 10, 15, 6]

    grafi = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    dimensionet = [40, 20, 30, 10, 30]

    shpjego_merge_sort(numrat)
    shpjego_fuqine_binare(3, 13)
    shpjego_dfs(grafi, "A")
    shpjego_zinxhirin_e_matricave(dimensionet)


if __name__ == "__main__":
    main()
