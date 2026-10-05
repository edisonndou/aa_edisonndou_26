# Task 2 - Trace i funksioneve reciproke m2 dhe mm.

from dataclasses import dataclass


@dataclass
class NumeruesiThirrjeve:
    thirrje: int = 0


def m2(n: int, numeruesi: NumeruesiThirrjeve) -> int:
    numeruesi.thirrje += 1

    if n < 0:
        raise ValueError("n duhet te jete numer jo negativ.")

    if n == 0:
        return 1

    return n - mm(m2(n - 1, numeruesi), numeruesi)


def mm(n: int, numeruesi: NumeruesiThirrjeve) -> int:
    numeruesi.thirrje += 1

    if n < 0:
        raise ValueError("n duhet te jete numer jo negativ.")

    if n == 0:
        return 0

    return n - m2(mm(n - 1, numeruesi), numeruesi)


def gjurmo_m2(n: int) -> tuple[int, int]:
    numeruesi = NumeruesiThirrjeve()
    rezultati = m2(n, numeruesi)

    return rezultati, numeruesi.thirrje


def shpjego_gjurmen_e_m2() -> None:
    n = 20
    kthimi_i_parashikuar = 12
    thirrjet_e_parashikuara = 1597
    rezultati, thirrjet = gjurmo_m2(n)

    print(f"m2({n})")
    print("Parashikimi para ekzekutimit:")
    print("- Kthen:", kthimi_i_parashikuar)
    print("- Thirrje:", thirrjet_e_parashikuara)
    print("Rezultati pas shtimit te numeruesit:")
    print("- Kthen:", rezultati)
    print("- Thirrje:", thirrjet)
    print("Pse gjurmimi eshte i veshtire?")
    print("- m2 therret mm dhe mm therret perseri m2.")
    print("- Argumenti i thirrjes se jashtme eshte rezultati i nje thirrjeje tjeter.")
    print("- Per shembull, m2(n - 1) duhet perfunduar para thirrjes se mm.")
    print("- Numeruesi perfshin thirrjet e m2 dhe mm.")


def main() -> None:
    shpjego_gjurmen_e_m2()


if __name__ == "__main__":
    main()
