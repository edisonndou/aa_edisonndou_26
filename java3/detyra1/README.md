# Java 3 - Detyra 1: Organizational Hierarchy Analysis

Zgjidhja eshte ne Python, sipas kerkeses se perdoruesit. Emrat publike te
funksioneve dhe fushat e rezultateve jane ruajtur si ne detyre, ku firmat jane
dhene ne TypeScript. `dict` zevendeson `Map`, `set` zevendeson `Set` dhe
`None` zevendeson `null`. Paga dhe shuma e pagave pranojne numra te plote ose
dhjetore, sipas tipit `number` ne dokument.

## Ekzekutimi

Kerkohet Python 3.10 ose me i ri, pa paketa shtese. Nga rrenja e projektit:

```powershell
python java3/detyra1/main.py
```

`employees.json` permban te 12 punonjesit e detyres. Skedari lexohet relativisht
me `main.py`, ndaj programi funksionon edhe nga nje drejtori tjeter.

Pas shpaketimit te ZIP-it, nga drejtoria qe permban skedaret:

```powershell
python main.py
```

## Zgjidhjet

1. **`getEmployeeDepth`** nderton nje indeks ID -> punonjes dhe ngjitet me
   rekursion te mbikeqyresi. CEO kthen 0; cdo kthim shton 1. ID e panjohur,
   mbikeqyresi qe mungon dhe ciklet kthejne -1, qe perhapet pa u shtuar.
2. **`getAllSubordinates`** nderton indeksin mbikeqyres -> femije. Rekursioni
   mbledh vartesit me thellesi relative duke filluar nga 1. Menaxheri nuk
   perfshihet; rezultati renditet sipas thellesise dhe pastaj ID-se.
3. **`getPathToCeo`** shton punonjesin ne rruge dhe therritet per mbikeqyresin.
   Shtimi ne te njejten liste shmang kopjimin e rruges ne cdo nivel. CEO
   perfshihet. Nese zinxhiri eshte i prishur ose ciklik, kthehet [] dhe jo
   nje rruge e pjesshme.
4. **`findLowestCommonManager`** kontrollon ID-te para llogaritjes, riperdor
   `getPathToCeo` saktesisht nje here per secilin punonjes, dhe kerkon me
   rekursion paraardhesin e pare te rruges se pare qe ndodhet ne `set` e
   rruges se dyte. Pozitat ne rruge japin distancat. Vete punonjesi mund te
   jete pergjigjja; pemet e ndara ose zinxhiret e pavlefshem japin `None`.
5. **`calculateTeamSalary`** llogarit pagen e punonjesit plus shumen e pagave
   te nenpemeve me rekursion. Menaxheri perfshihet; ID e panjohur jep 0.

Traversimet jane rekursive. Ciklet iterative perdoren vetem per indekset,
femijet e nje nyjeje dhe paraqitjen/renditjen. `visited` parandalon ciklet dhe
numerimin e dyfishte; asnje funksion nuk ndryshon te dhenat hyrse.
Supozohen ID unike dhe objekte qe respektojne skemen e detyres.

## Kompleksiteti

`n` = numri i punonjesve, `h` = gjatesia maksimale e zinxhirit,
`k` = numri i vartesve te menaxherit.

| Funksioni | Koha, perfshire indeksimin | Hapesira ndihmese |
| --- | --- | --- |
| `getEmployeeDepth` | O(n + h), traversimi O(h) | O(n + h) |
| `getAllSubordinates` | O(n + k log k) | O(n + h + k) |
| `getPathToCeo` | O(n + h), traversimi O(h) | O(n + h) |
| `findLowestCommonManager` | O(n + h1 + h2) | O(n + h1 + h2) |
| `calculateTeamSalary` | O(n + k) | O(n + h + k) |

Indeksimet e perseritura nga riperdorimi i `getPathToCeo` mbeten O(n) gjithsej.
Ne Python, nje hierarki shume e thelle mund te arrije kufirin e rekursionit;
programi nuk e ndryshon kufirin global.

## Rezultatet e shembullit kryesor

- Thellesia e Liam: `4`.
- Vartesit e Bob, si `(id, relative_depth)`:
  `(4, 1), (5, 1), (7, 2), (8, 2), (9, 2), (10, 2), (12, 3)`.
- Rruga e Liam: `[12, 7, 4, 2, 1]`.
- Menaxheri i perbashket i Liam dhe Ivy: Bob Smith, ID `2`, distancat `3` dhe `2`.
- Paga totale e organizates: `1490000`.

Pagat e tjera te dhena ne detyre: David `505000`, Grace `170000`,
Liam `50000`, ID e panjohur `0`.

## Rastet e testimit te Problemit 5

`test_team_salary.py` permban kater testet e kerkuara nga detyra:

| Rasti | ID | Paga totale e pritur |
| --- | --- | --- |
| CEO, e gjithe organizata | 1 | 1490000 |
| Menaxher i ndermjetem, perfshire vartesit indirekte | 4 | 505000 |
| Punonjes pa vartes, vetem paga e tij | 12 | 50000 |
| ID qe nuk ekziston | 999 | 0 |

Testet perdorin `unittest` nga biblioteka standarde dhe dataset-in e detyres.
Komanda per ekzekutimin e tyre nga rrenja e projektit eshte:

```powershell
python -m unittest discover -s java3/detyra1 -p test_team_salary.py -v
```

Pas shpaketimit te ZIP-it, nga drejtoria qe permban skedaret:

```powershell
python -m unittest discover -s . -p test_team_salary.py -v
```

Testet jane perfshire per te plotesuar kerkesen e dokumentit. Nuk jane
ekzekutuar gjate pergatitjes se dorezimit.
