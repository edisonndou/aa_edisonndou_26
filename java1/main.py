# Detyra 1. Tre funksione që nuk janë algoritme sortimi ose kërkimi.

# Shumëzon dy matrica katrore me madhësi të njëjtë.
def shumezimi_i_matricave(
    matrica_a: list[list[int]],
    matrica_b: list[list[int]],
) -> list[list[int]]:
    madhesia = len(matrica_a)
    rezultati = [[0] * madhesia for _ in range(madhesia)]

    for rreshti in range(madhesia):
        for kolona in range(madhesia):
            for pozita in range(madhesia):
                rezultati[rreshti][kolona] += (
                    matrica_a[rreshti][pozita] * matrica_b[pozita][kolona]
                )

    return rezultati


# Llogarit numrin minimal të ndryshimeve për ta kthyer një tekst në një tjetër.
def distanca_levenshtein(teksti_i_pare: str, teksti_i_dyte: str) -> int:
    rreshti_paraardhes = list(range(len(teksti_i_dyte) + 1))

    for indeksi_i_pare, shkronja_e_pare in enumerate(teksti_i_pare, start=1):
        rreshti_aktual = [indeksi_i_pare]

        for indeksi_i_dyte, shkronja_e_dyte in enumerate(teksti_i_dyte, start=1):
            kostoja = 0 if shkronja_e_pare == shkronja_e_dyte else 1
            rreshti_aktual.append(min(
                rreshti_aktual[-1] + 1,
                rreshti_paraardhes[indeksi_i_dyte] + 1,
                rreshti_paraardhes[indeksi_i_dyte - 1] + kostoja,
            ))

        rreshti_paraardhes = rreshti_aktual

    return rreshti_paraardhes[-1]


# Kthen hapat për zgjidhjen e problemit Kullat e Hanoit.
def kullat_e_hanoit(
    numri_i_disqeve: int,
    burimi: str,
    destinacioni: str,
    ndihmesi: str,
) -> list[str]:
    hapat = []

    def zhvendos(disqet: int, nga: str, tek: str, me_ndihmen_e: str) -> None:
        if disqet <= 0:
            return

        zhvendos(disqet - 1, nga, me_ndihmen_e, tek)
        hapat.append(f"Zhvendos diskun {disqet}: {nga} -> {tek}")
        zhvendos(disqet - 1, me_ndihmen_e, tek, nga)

    zhvendos(numri_i_disqeve, burimi, destinacioni, ndihmesi)

    return hapat


def main() -> None:
    matrica_a = [[1, 2], [3, 4]]
    matrica_b = [[5, 6], [7, 8]]

    print("Funksioni 1:")
    print("Dalja:", shumezimi_i_matricave(matrica_a, matrica_b))
    print("Rasti më i mirë kohor: O(n³)")
    print("Rasti më i keq kohor: O(n³)")
    print("Big-O hapësinor: O(n²)")

    print("\nFunksioni 2:")
    print("Dalja:", distanca_levenshtein("mace", "male"))
    print("Rasti më i mirë kohor: O(m + n), kur njëri tekst është bosh")
    print("Rasti më i keq kohor: O(m × n)")
    print("Big-O hapësinor: O(n)")

    print("\nFunksioni 3:")
    print("Dalja:")

    for hapi in kullat_e_hanoit(3, "A", "C", "B"):
        print(hapi)

    print("Rasti më i mirë kohor: O(2ⁿ)")
    print("Rasti më i keq kohor: O(2ⁿ)")
    print("Big-O hapësinor: O(2ⁿ)")


if __name__ == "__main__":
    main()
