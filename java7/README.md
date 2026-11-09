# Java 7 - Tabelat hash

## Çfarë kërkohej dhe çfarë bëmë?

Duhej të ruanim dhe të gjenim vlera me tabela hash, të trajtonim vlerat që duan të njëjtin vend, të fshinim pa prishur kërkimin, të krahasonim mënyrat dhe ta zmadhonim tabelën kur mbushet shumë.

Në `task1` ndërtuam mënyrat bazë dhe treguam problemin gjatë fshirjes. Në `task2` e zgjidhëm atë dhe shtuam double hashing, krahasimin e mënyrave dhe zmadhimin. Kodi është në Python.

`key` është vlera që ruajmë, `table` është tabela dhe `m` numri i vendeve. Hash-i tregon nga cili vend të fillojmë. Kur ai vend është i zënë, duhet një mënyrë për të ruajtur edhe vlerën tjetër.

## task1 - Mënyrat bazë

| Skedari dhe funksioni | Çfarë kërkohej dhe çfarë bëmë? | Pse e përdorëm? |
| --- | --- | --- |
| `detyra1.py`: `num(key)` | Për fjalët mbledhim vlerat A=1, B=2, deri te Z=26. Numri mbetet siç është. | Që edhe fjalët të marrin vlerë numerike. |
| `detyra1.py`: `h(key, m)` | Llogarisim `num(key) % m`, pra mbetjen e pjesëtimit. | Që të zgjedhim një vend brenda tabelës. |
| `detyra1.py`: `chainedTable(keys, m)` | Krijojmë një listë në çdo vend. Vlerat me të njëjtin hash hyjnë në të njëjtën listë. | Që disa vlera të ndajnë të njëjtin vend pa humbur asnjërën. |
| `detyra2.py`: `probeInsert(table, key)` | Nëse vendi është i zënë, provojmë vendin pasues derisa të gjejmë një bosh. Kthejmë pozicionin. | Që të ruajmë vlerën pa lista brenda tabelës. |
| `detyra2.py`: `probeFind(table, key)` | Kërkojmë një nga një nga vendi fillestar. Kthejmë pozicionin ose `-1` nëse nuk gjendet. | Që të gjejmë edhe vlerat që u vendosën më tej. |
| `detyra3.py`: `probeRemove(table, key)` | Gjejmë vlerën dhe vendin e saj e bëjmë `None`, pra bosh. | Për të treguar fshirjen fillestare dhe problemin që krijon. |

Pas fundit të tabelës vazhdojmë nga fillimi. Nëse nuk ka vend të lirë, `probeInsert` jep gabim.

### task1/detyra4.py - Shembulli hap pas hapi

Nuk ka funksione të reja. Skedari ndërton tabelën dhe krahason parashikimet me pesë rezultate: listën në vendin 11, kërkimin e `PARTED`, kërkimin e `KID`, fshirjen e `ARE` dhe kërkimin e `SOON`.

**Problemi:** Pas fshirjes së `ARE` me `None`, kërkimi ndalet te vendi bosh dhe nuk arrin te `SOON`, megjithëse ajo është ende në tabelë.

## task2/detyra1.py - Fshirja pa prishur kërkimin

| Funksioni ose shenja | Çfarë kërkohej dhe çfarë bëmë? | Pse e përdorëm? |
| --- | --- | --- |
| `num(key)` | E kthejmë fjalën në numër si te `task1`. | Që të llogarisim vendin e vlerës. |
| `h(key, m)` | Përdorim përsëri mbetjen e pjesëtimit me `m`. | Që vendosja dhe kërkimi të fillojnë në të njëjtin vend. |
| `chainedTable(keys, m)` | Ruajmë vlerat në lista sipas hash-it. | Që ta krahasojmë këtë mënyrë me të tjerat. |
| `DELETED` | Krijojmë një shenjë të veçantë për një vend të fshirë. | Që ta dallojmë nga një vend që ka qenë bosh. |
| `probeInsert(table, key)` | Lejojmë vendosjen te `None` ose `DELETED`. Provojmë jo më shumë se `m` vende. | Që vendet e fshira të ripërdoren dhe kërkimi të mos vazhdojë pa fund. |
| `probeFind(table, key)` | Kalojmë mbi `DELETED`, por ndalemi te `None`. | Që të gjejmë vlerat pas një vendi të fshirë. |
| `probeRemove(table, key)` | Ruajmë mënyrën e vjetër që shkruan `None`. | Për krahasim; problemi i saj mbetet. |
| `remove(table, key)` | Shkruajmë `DELETED` në vendin e vlerës. Kthejmë pozicionin ose `-1`, pa ndryshuar madhësinë. | Që të fshijmë vlerën dhe të mbajmë të hapur rrugën e kërkimit. |

## task2/detyra2.py - Double hashing

Në vend që të ecim gjithmonë nga një vend, llogarisim hapin nga vlera: `s = m - 2 - num(key) % (m - 2)`.

| Funksioni | Çfarë kërkohej dhe çfarë bëmë? | Pse e përdorëm? |
| --- | --- | --- |
| `doubleHashInsert(table, key)` | Kur vendi është i zënë, ecim me hapin e llogaritur deri te një vend bosh ose i fshirë. Kthejmë pozicionin. | Që vlerat të mos grumbullohen aq shumë pranë njëra-tjetrës. |
| `doubleHashFind(table, key)` | Ndjekim të njëjtët hapa si gjatë vendosjes. Kthejmë pozicionin ose `-1`. | Që të kërkojmë pikërisht aty ku mund të jetë ruajtur vlera. |
| `displayTable(table)` | Shfaqim pozicionet dhe vlerat; shenjën e fshirjes e tregojmë si `DELETED`. | Që ta lexojmë më lehtë tabelën. |

Duhet `m > 2`. Përdor madhësi numër të thjeshtë, si 11 ose 13, që hapat të arrijnë çdo vend. Kodi nuk e kontrollon nëse madhësia është numër i thjeshtë. Funksioni linear `remove` nuk duhet përdorur për fshirje në double hashing.

## task2/detyra3.py - Krahasimi i mënyrave

| Funksioni | Çfarë kërkohej dhe çfarë bëmë? | Pse e përdorëm? |
| --- | --- | --- |
| `maxComparisons(keys, m)` | Ndërtojmë tri tabelat dhe gjejmë numrin më të madh të krahasimeve për një kërkim të suksesshëm. Kthejmë `chained`, `linear` dhe `double`. | Që të krahasojmë punën e tri mënyrave mbi të njëjtat vlera. |

Vlerat duhet të jenë të ndryshme, më pak se `m`, dhe `m > 2`. Lista hyrëse nuk ndryshohet.

## task2/detyra4.py - Zmadhimi i tabelës

| Funksioni | Çfarë kërkohej dhe çfarë bëmë? | Pse e përdorëm? |
| --- | --- | --- |
| `isPrime(n)` | Kontrollojmë nëse `n` pjesëtohet vetëm me 1 dhe me vetveten. Numrat nën 2 nuk pranohen. | Që të njohim numrat e thjeshtë. |
| `nextPrime(n)` | Gjejmë numrin e parë të thjeshtë që është të paktën `n`. | Që të zgjedhim madhësinë e re. |
| `insertGrow(table, key)` | Nëse shtimi do ta mbushte mbi gjysmën, zmadhojmë në `nextPrime(2*m)`, rivendosim vlerat e vjetra sipas rendit të vendeve dhe shtojmë të renë. `None` dhe `DELETED` nuk numërohen si vlera aktive. | Që tabela të ketë më shumë vende të lira; rivendosja llogarit pozicionet për madhësinë e re. |
| `displayTable(table)` | Shfaqim pozicionet dhe vlerat pas ndryshimeve. | Që të shohim rezultatin e zmadhimit. |

Ruajmë rezultatin me `table = insertGrow(table, key)`, sepse zmadhimi krijon listë të re. Funksioni refuzon tabelën bosh. Kufiri i mbushjes 0.5 supozon një tabelë që e respektonte kufirin para shtimit; një zmadhim i vetëm nuk rregullon domosdoshmërisht çdo tabelë tashmë shumë të mbushur.

## Përdorimi

Shembujt përdorin fjalë me shkronja të mëdha ose numra të plotë. Megjithëse `num` pranon edhe numra me presje, ata nuk duhen përdorur si pozicione të listës.

```powershell
python java7/task1/detyra1.py
```

Skedarët hapen drejtpërdrejt që importet të përdorin dosjen e duhur `task1` ose `task2`. Disa skedarë ekzistues kanë `assert`; `task1/detyra4.py` e kryen shembullin edhe kur importohet. Gjatë këtij rikrijimi nuk u shkruan dhe nuk u ekzekutuan teste.
