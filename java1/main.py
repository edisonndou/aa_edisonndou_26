# Detyra 1. Tre funksione që nuk janë algoritme sortimi ose kërkimi.

# Kthen shumën e të gjithë elementeve të listës.
def shuma_e_elementeve(numrat: list[int]) -> int:
    shuma = 0

    for numer in numrat:
        shuma += numer

    return shuma


# Llogarit fuqinë me metodën e përgjysmimit të eksponentit.
def fuqia(baza: float, eksponenti: int) -> float:
    if eksponenti < 0:
        raise ValueError("Eksponenti duhet të jetë jo negativ.")

    rezultati = 1.0

    while eksponenti > 0:
        if eksponenti % 2 == 1:
            rezultati *= baza

        baza *= baza
        eksponenti //= 2

    return rezultati


# Kthen të gjitha çiftet e mundshme të elementeve të listës.
def ciftet_e_elementeve(numrat: list[int]) -> list[tuple[int, int]]:
    ciftet = []

    for indeksi_i_pare in range(len(numrat)):
        for indeksi_i_dyte in range(indeksi_i_pare + 1, len(numrat)):
            ciftet.append((numrat[indeksi_i_pare], numrat[indeksi_i_dyte]))

    return ciftet


def main() -> None:
    numrat = [2, 4, 6, 8]

    print("Funksioni 1:")
    print("Dalja:", shuma_e_elementeve(numrat))
    print("Big-O kohor: O(n). Kompleksiteti kohor: O(n), sepse çdo element vizitohet një herë.")
    print("Big-O hapësinor: O(1). Kompleksiteti hapësinor: O(1), sepse përdoret vetëm një variabël shtesë.")

    print("\nFunksioni 2:")
    print("Dalja:", fuqia(2, 10))
    print("Big-O kohor: O(log n). Kompleksiteti kohor: O(log n), sepse eksponenti përgjysmohet në çdo hap.")
    print("Big-O hapësinor: O(1). Kompleksiteti hapësinor: O(1), sepse përdoret një numër konstant variablash.")

    print("\nFunksioni 3:")
    print("Dalja:", ciftet_e_elementeve(numrat))
    print("Big-O kohor: O(n²). Kompleksiteti kohor: O(n²), për shkak të dy cikleve të ndërthurura.")
    print("Big-O hapësinor: O(n²). Kompleksiteti hapësinor: O(n²), sepse ruhen n(n - 1) / 2 çifte.")


if __name__ == "__main__":
    main()
