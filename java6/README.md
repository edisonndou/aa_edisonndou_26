# Java 6 - Kërkimi në tekst

## Çfarë kërkohej dhe çfarë bëmë?

Duhej të gjenim një fjalë ose pjesë teksti brenda një teksti tjetër, të numëronim krahasimet, të gjenim të gjitha paraqitjet dhe t'i shënonim me kllapa. Implementuam disa algoritme me krahasime shkronjash, pa kërkim, zëvendësim, ndarje teksti ose regex të gatshëm. Zgjidhjet janë në Python dhe ndahen në pesë detyra.

`T` është teksti ku kërkojmë; `P` është pjesa që kërkojmë. Pozicionet fillojnë nga `0`. Kërkimi i parë kthen `-1` kur nuk gjen përputhje.

## detyra1/main.py - Kërkimi dhe numërimi

| Funksioni | Çfarë kërkohej dhe çfarë bëmë? | Pse e përdorëm? |
| --- | --- | --- |
| `resetCounters()` | Kthejmë numëruesit në zero. | Që matja e re të mos përzihet me të vjetrën. |
| `getCounters()` | Marrim numrin e krahasimeve dhe të pozicioneve të provuara. | Që të shohim sa punë bëri kërkimi. |
| `record_alignment()` | Numërojmë një vendosje të fjalës mbi tekst. | Që të dimë sa pozicione provuam. |
| `compare_characters(a, b)` | Krahasojmë dy shkronja dhe numërojmë krahasimin, edhe kur ndryshojnë. | Që çdo algoritëm të matet njësoj. |
| `bruteForce(T, P)` | Provojmë çdo pozicion një nga një dhe kthejmë përputhjen e parë. | Është mënyra më e thjeshtë për të kuptuar kërkimin. |
| `shiftTable(P)` | Ndërtojmë një tabelë që tregon sa mund ta lëvizim fjalën sipas shkronjës. Shkronjën e fundit nuk e përfshijmë. | Që të kapërcejmë pozicione pa i provuar të gjitha. |
| `horspool(T, P)` | Krahasojmë nga fundi i fjalës dhe lëvizim sipas shkronjës në fund të pjesës së tekstit që po kontrollojmë. | Shpesh bën më pak krahasime se kërkimi i thjeshtë. |
| `horspool2(T, P)` | Ruajmë variantin e ligjëratës që lëviz sipas shkronjës ku ndodhi dallimi. | Për ta krahasuar me Horspool; ky variant mund të kapërcejë përputhje të sakta. |

## detyra2/main.py - Të gjitha paraqitjet

| Funksioni | Çfarë kërkohej dhe çfarë bëmë? | Pse e përdorëm? |
| --- | --- | --- |
| `findAll(T, P)` | Vazhdojmë kërkimin pas çdo gjetjeje dhe mbledhim të gjitha pozicionet, edhe kur paraqitjet mbivendosen. | Që të mos ndalemi te gjetja e parë. |

Shembull: `findAll('banana', 'ana')` jep `[1, 3]`.

## detyra3/main.py - Shënimi me kllapa

| Funksioni | Çfarë kërkohej dhe çfarë bëmë? | Pse e përdorëm? |
| --- | --- | --- |
| `highlight(T, P)` | Përdorim `findAll` dhe vendosim kllapa rreth paraqitjeve që nuk mbivendosen. | Që pjesa e gjetur të dallohet në tekst. |

Shembull: `highlight('banana', 'ana')` jep `b[ana]na`. Paraqitjen e dytë nuk e shënojmë sepse mbivendoset me të parën.

## detyra4/main.py - Pjesa në fund që përputhet

| Funksioni | Çfarë kërkohej dhe çfarë bëmë? | Pse e përdorëm? |
| --- | --- | --- |
| `goodSuffixTable(P)` | Përgatisim lëvizjet sipas pjesës në fund të fjalës që tashmë u përputh. Kërkojmë të njëjtën pjesë më herët ose një fillim që përputhet me fundin. Nëse nuk ka, lëvizim sa gjatësia e fjalës. | Që të përdorim informacionin e gjetur dhe të shmangim krahasime të panevojshme. |

## detyra5/main.py - Bashkimi i dy rregullave

| Funksioni | Çfarë kërkohej dhe çfarë bëmë? | Pse e përdorëm? |
| --- | --- | --- |
| `boyerMoore(T, P)` | Bashkojmë rregullin e shkronjës që nuk përputhet me `goodSuffixTable` dhe zgjedhim lëvizjen më të madhe të sigurt. | Që kërkimi të kapërcejë më shumë pozicione të panevojshme. |

Teksti i detyrës 5 përsëriste detyrën 4. Implementuam `boyerMoore`, sepse ishte në listën e funksioneve të kërkuara.

## search.py dhe përdorimi

`search.py` i mbledh funksionet për t'i importuar nga një vend; nuk shton funksione të reja. `__all__` përcakton listën publike të tyre.

Nga dosja kryesore e projektit:

```powershell
python -m java6.detyra1.main
```

Për detyrat e tjera përdor `detyra2` deri te `detyra5`. Nuk duhen paketa shtesë.

Kërkimi dallon shkronjat e mëdha nga të voglat. Për një fjalë bosh, kërkimi i parë kthen `0`, `findAll` kthen çdo kufi mes shkronjave, ndërsa `highlight` nuk ndryshon tekstin. Numëruesit mblidhen deri te `resetCounters()`; përgatitja e tabelave nuk shton krahasime kërkimi. Për kërkim të saktë përdor `horspool` ose `boyerMoore`, jo variantin mësimor `horspool2`.

Gjatë këtij rikrijimi nuk u shkruan dhe nuk u ekzekutuan teste.
