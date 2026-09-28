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


# Kontrollon nëse teksti lexohet njësoj nga të dy drejtimet.
def eshte_palindrom(teksti: str) -> tuple[bool, int]:
    numri_i_krahasimeve = 0

    for indeksi in range(len(teksti) // 2):
        numri_i_krahasimeve += 1

        if teksti[indeksi] != teksti[-indeksi - 1]:
            return False, numri_i_krahasimeve

    return True, numri_i_krahasimeve


# Kontrollon nëse një matricë katrore është simetrike.
def eshte_matrice_simetrike(
    matrica: list[list[int]],
) -> tuple[bool, int]:
    numri_i_krahasimeve = 0

    for rreshti in range(len(matrica)):
        for kolona in range(rreshti + 1, len(matrica)):
            numri_i_krahasimeve += 1

            if matrica[rreshti][kolona] != matrica[kolona][rreshti]:
                return False, numri_i_krahasimeve

    return True, numri_i_krahasimeve


# Ndërron rreshtat me kolonat e një matrice katrore.
def transpozo_matricen(
    matrica: list[list[int]],
) -> tuple[list[list[int]], int]:
    madhesia = len(matrica)
    matrica_e_transpozuar = [[0] * madhesia for _ in range(madhesia)]
    numri_i_caktimeve = 0

    for rreshti in range(madhesia):
        for kolona in range(madhesia):
            matrica_e_transpozuar[kolona][rreshti] = matrica[rreshti][kolona]
            numri_i_caktimeve += 1

    return matrica_e_transpozuar, numri_i_caktimeve


# Rendit numra të plotë jo negativë sipas shifrave të tyre.
def radix_sort(numrat: list[int]) -> tuple[list[int], int, int]:
    if any(numer < 0 for numer in numrat):
        raise ValueError("Radix Sort pranon vetëm numra jo negativë.")

    if not numrat:
        return [], 0, 0

    rezultati = numrat[:]
    shifra = 1
    kalimet = 0
    perpunimet = 0
    numri_me_i_madh = max(rezultati)

    while numri_me_i_madh // shifra > 0:
        numerimi = [0] * 10
        dalje = [0] * len(rezultati)

        for numer in rezultati:
            shifra_aktuale = (numer // shifra) % 10
            numerimi[shifra_aktuale] += 1
            perpunimet += 1

        for indeksi in range(1, 10):
            numerimi[indeksi] += numerimi[indeksi - 1]

        for numer in reversed(rezultati):
            shifra_aktuale = (numer // shifra) % 10
            numerimi[shifra_aktuale] -= 1
            dalje[numerimi[shifra_aktuale]] = numer

        rezultati = dalje
        shifra *= 10
        kalimet += 1

    return rezultati, kalimet, perpunimet


# Rendit duke zgjedhur elementin e fundit si pivot.
def quick_sort(numrat: list[int]) -> tuple[list[int], int]:
    rezultati = numrat[:]
    krahasimet = 0

    def ndaj(fillimi: int, fundi: int) -> int:
        nonlocal krahasimet
        pivot = rezultati[fundi]
        pozita_e_pivotit = fillimi

        for indeksi in range(fillimi, fundi):
            krahasimet += 1

            if rezultati[indeksi] <= pivot:
                rezultati[pozita_e_pivotit], rezultati[indeksi] = (
                    rezultati[indeksi],
                    rezultati[pozita_e_pivotit],
                )
                pozita_e_pivotit += 1

        rezultati[pozita_e_pivotit], rezultati[fundi] = (
            rezultati[fundi],
            rezultati[pozita_e_pivotit],
        )

        return pozita_e_pivotit

    def rendit(fillimi: int, fundi: int) -> None:
        if fillimi >= fundi:
            return

        pozita_e_pivotit = ndaj(fillimi, fundi)
        rendit(fillimi, pozita_e_pivotit - 1)
        rendit(pozita_e_pivotit + 1, fundi)

    rendit(0, len(rezultati) - 1)

    return rezultati, krahasimet


def main() -> None:
    matrica_a = [[1, 2], [3, 4]]
    matrica_b = [[5, 6], [7, 8]]

    print("Funksioni 1:")
    print("Dalja:", shumezimi_i_matricave(matrica_a, matrica_b))
    # print("Rasti më i mirë kohor: O(n³)")
    print("Rasti më i keq kohor: O(n³)")
    print("Big-O hapësinor: O(n²)")

    print("\nFunksioni 2:")
    print("Dalja:", distanca_levenshtein("mace", "male"))
    print("Rasti më i mirë kohor: O(m + n), kur njëri tekst është bosh")
    # print("Rasti më i keq kohor: O(m × n)")
    print("Big-O hapësinor: O(n)")

    print("\nFunksioni 3:")
    print("Dalja:")

    for hapi in kullat_e_hanoit(3, "A", "C", "B"):
        print(hapi)

    print("Rasti më i mirë kohor: O(2ⁿ)")
    print("Rasti më i keq kohor: O(2ⁿ)")
    print("Big-O hapësinor: O(2ⁿ)")

    teksti_me_i_mire = "abcdef"
    teksti_me_i_keq = "abccba"
    rezultati_me_i_mire, krahasimet_me_te_mira = eshte_palindrom(
        teksti_me_i_mire,
    )
    rezultati_me_i_keq, krahasimet_me_te_keqija = eshte_palindrom(
        teksti_me_i_keq,
    )

    print("\nFunksioni 4 - Kontrolli i palindromit:")
    print("\nEkzekutimi në rastin më të mirë:")
    print("Hyrja:", teksti_me_i_mire)
    print("Dalja:", rezultati_me_i_mire)
    print("Numri i krahasimeve:", krahasimet_me_te_mira)
    print("Kompleksiteti kohor: O(1)")

    print("\nEkzekutimi në rastin më të keq:")
    print("Hyrja:", teksti_me_i_keq)
    print("Dalja:", rezultati_me_i_keq)
    print("Numri i krahasimeve:", krahasimet_me_te_keqija)
    print("Kompleksiteti kohor: O(n)")

    print("\nNdryshimi mes rasteve:")
    print("Rasti më i mirë ndalet pas mospërputhjes së parë.")
    print("Rasti më i keq kontrollon n / 2 çifte shkronjash.")
    print("Dallimi në krahasime:", krahasimet_me_te_keqija - krahasimet_me_te_mira)
    print("Big-O hapësinor për të dy rastet: O(1)")

    matrica_rasti_me_i_keq = [
        [1, 2, 3, 4],
        [2, 5, 6, 7],
        [3, 6, 8, 9],
        [4, 7, 9, 10],
    ]
    matrica_rasti_me_i_mire = [
        rreshti[:] for rreshti in matrica_rasti_me_i_keq
    ]

    # Ndryshohet vetëm kjo vlerë: [0][1] bëhet 99, ndërsa [1][0] mbetet 2.
    # Kështu funksioni gjen mospërputhjen që në krahasimin e parë.
    matrica_rasti_me_i_mire[0][1] = 99

    rezultati_me_i_mire, krahasimet_me_te_mira = eshte_matrice_simetrike(
        matrica_rasti_me_i_mire,
    )
    rezultati_me_i_keq, krahasimet_me_te_keqija = eshte_matrice_simetrike(
        matrica_rasti_me_i_keq,
    )
    matrica_e_transpozuar, caktimet = transpozo_matricen(
        matrica_rasti_me_i_keq,
    )

    print("\nFunksionet 5 dhe 6 - Krahasimi:")
    print("Të dy funksionet kanë rastin më të keq kohor O(n²).")
    print("Funksioni 5 është më i mirë në rastin më të mirë: O(1),")
    print("sepse ndalet sapo gjen dy vlera jo simetrike.")
    print("Funksioni 6 është gjithmonë O(n²), sepse transpozon çdo element.")

    print("\nFunksioni 5 - Kontrolli i simetrisë:")

    print("Rasti më i mirë O(1):")
    print("Inputi:", matrica_rasti_me_i_mire)
    print("Inputi i ndryshuar: matrica[0][1] = 99")
    print("Dalja:", rezultati_me_i_mire)
    print("Numri i krahasimeve:", krahasimet_me_te_mira)
    print("Pse: 99 nuk është e barabartë me matrica[1][0], që është 2,")
    print("prandaj funksioni ndalet pas krahasimit të parë.")

    print("\nRasti më i keq O(n²):")
    print("Inputi:", matrica_rasti_me_i_keq)
    print("Dalja:", rezultati_me_i_keq)
    print("Numri i krahasimeve:", krahasimet_me_te_keqija)
    print("Pse: matrica është simetrike dhe nuk gjendet mospërputhje,")
    print("prandaj kontrollohen të gjitha n(n - 1) / 2 = 6 çiftet.")

    print("\nFunksioni 6 - Transpozimi i matricës:")
    print("Dalja:", matrica_e_transpozuar)
    print("Numri i caktimeve:", caktimet)
    print("Rasti më i mirë: O(n²)")
    print("Rasti më i keq: O(n²)")
    print("Inputi që ndikon: madhësia n e matricës, jo vlerat brenda saj.")
    print("Pse: çdo element duhet kopjuar, prandaj për n = 4")
    print("kryhen n² = 16 caktime pavarësisht vlerave të elementeve.")

    # Para ndërhyrjes, vlerat 0-499 janë në rend të përzier.
    inputi_para_nderhyrjes = [
        (indeksi * 137) % 500 for indeksi in range(500)
    ]

    # Ndërhyrja: të njëjtat vlera vendosen në rend rritës.
    # Kjo e çon Quick Sort-in me pivot të fundit në rastin më të keq.
    inputi_pas_nderhyrjes = sorted(inputi_para_nderhyrjes)

    _, radix_kalimet_para, radix_perpunimet_para = radix_sort(
        inputi_para_nderhyrjes,
    )
    _, quick_krahasimet_para = quick_sort(inputi_para_nderhyrjes)
    _, radix_kalimet_pas, radix_perpunimet_pas = radix_sort(
        inputi_pas_nderhyrjes,
    )
    _, quick_krahasimet_pas = quick_sort(inputi_pas_nderhyrjes)

    print("\nRadix Sort kundër Quick Sort:")
    print("Të dy rastet përdorin të njëjtat 500 vlera: 0 deri në 499.")

    print("\nRasti 1 - Para ndërhyrjes:")
    print("Inputi është i përzier:", inputi_para_nderhyrjes[:10], "...")
    print("Radix Sort - kalime:", radix_kalimet_para)
    print("Radix Sort - përpunime:", radix_perpunimet_para)
    print("Quick Sort - krahasime:", quick_krahasimet_para)
    print("Rendi i përzier mundëson ndarje më të balancuara se rasti i dytë.")

    print("\nNdërhyrja në input:")
    print("Inputi i përzier renditet para se t'u dërgohet algoritmeve.")
    print("Ndryshon vetëm renditja; numri dhe vlerat mbeten të njëjta.")

    print("\nRasti 2 - Pas ndërhyrjes:")
    print("Inputi është i renditur:", inputi_pas_nderhyrjes[:10], "...")
    print("Radix Sort - kalime:", radix_kalimet_pas)
    print("Radix Sort - përpunime:", radix_perpunimet_pas)
    print("Quick Sort - krahasime:", quick_krahasimet_pas)
    print("Quick Sort kalon në rastin më të keq O(n²).")

    print("\nNdikimi i ndërhyrjes:")
    print(
        "Shtesa e krahasimeve te Quick Sort:",
        quick_krahasimet_pas - quick_krahasimet_para,
    )
    print(
        "Ndryshimi i përpunimeve te Radix Sort:",
        radix_perpunimet_pas - radix_perpunimet_para,
    )
    print("Radix Sort nuk ndikohet nga renditja e inputit.")
    print("Quick Sort ndikohet sepse pivot-i i fundit është gjithmonë")
    print("vlera më e madhe dhe krijon ndarje n - 1 me 0 elemente.")


if __name__ == "__main__":
    main()
