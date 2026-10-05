# Task 3 - Trace i funksionit rekursiv m3.

from dataclasses import dataclass


@dataclass
class NumeruesiThirrjeve:
    thirrje: int = 0


def m3(n: int, numeruesi: NumeruesiThirrjeve) -> int:
    numeruesi.thirrje += 1

    if n <= 1:
        return 1

    return m3(n - 1, numeruesi) + m3(n - 1, numeruesi)


def gjurmo_m3(n: int) -> tuple[int, int]:
    numeruesi = NumeruesiThirrjeve()
    rezultati = m3(n, numeruesi)

    return rezultati, numeruesi.thirrje


def shpjego_gjurmen_e_m3() -> None:
    n = 20
    kthimi_i_parashikuar = 2 ** (n - 1)
    thirrjet_e_parashikuara = 2 ** n - 1
    rezultati, thirrjet = gjurmo_m3(n)

    print(f"m3({n})")
    print("Parashikimi para ekzekutimit:")
    print("- Kthen:", kthimi_i_parashikuar)
    print("- Thirrje:", thirrjet_e_parashikuara)
    print("Rezultati pas shtimit te numeruesit:")
    print("- Kthen:", rezultati)
    print("- Thirrje:", thirrjet)
    print("Pse?")
    print("- Cdo thirrje me n > 1 krijon dy thirrje identike me n - 1.")
    print("- Rezultati dyfishohet ne cdo nivel: m3(n) = 2^(n - 1).")
    print("- Pema ka n nivele dhe 2^n - 1 thirrje gjithsej.")
    print("- Te njejtat nenprobleme llogariten perseri, pa memoizim.")
    print("- Time complexity: O(2^n); space complexity: O(n).")


def main() -> None:
    shpjego_gjurmen_e_m3()


if __name__ == "__main__":
    main()
