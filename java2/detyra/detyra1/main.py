# Task 1 - Trace i funksionit rekursiv m1.

from dataclasses import dataclass


@dataclass
class NumeruesiThirrjeve:
    thirrje: int = 0


def m1(vlerat: list[int], numeruesi: NumeruesiThirrjeve) -> int:
    numeruesi.thirrje += 1

    if len(vlerat) <= 1:
        return len(vlerat)

    mesi = len(vlerat) >> 1

    return (
        m1(vlerat[:mesi], numeruesi)
        + m1(vlerat[mesi:], numeruesi)
        + 1
    )


def gjurmo_m1(gjatesia: int) -> tuple[int, int]:
    if gjatesia < 0:
        raise ValueError("Gjatesia nuk mund te jete negative.")

    numeruesi = NumeruesiThirrjeve()
    rezultati = m1(list(range(gjatesia)), numeruesi)

    return rezultati, numeruesi.thirrje


def shpjego_gjurmen(gjatesia: int) -> None:
    kthimi_i_parashikuar = 0 if gjatesia == 0 else 2 * gjatesia - 1
    thirrjet_e_parashikuara = 1 if gjatesia == 0 else 2 * gjatesia - 1
    rezultati, thirrjet = gjurmo_m1(gjatesia)

    print(f"m1, gjatesia {gjatesia}")
    print("Parashikimi para ekzekutimit:")
    print("- Kthen:", kthimi_i_parashikuar)
    print("- Thirrje:", thirrjet_e_parashikuara)
    print("Rezultati pas shtimit te numeruesit:")
    print("- Kthen:", rezultati)
    print("- Thirrje:", thirrjet)
    print("Pse?")
    print("- Funksioni e ndan vargun derisa secila pjese ka nje element.")
    print(f"- Krijohen {gjatesia} gjethe dhe {max(gjatesia - 1, 0)} ndarje.")
    print("- Prandaj kthimi dhe thirrjet jane 2n - 1 per n >= 1.")


def main() -> None:
    shpjego_gjurmen(8)

    print("\nVlera e permendur ne tabelen e detyres:")
    shpjego_gjurmen(3)


if __name__ == "__main__":
    main()
