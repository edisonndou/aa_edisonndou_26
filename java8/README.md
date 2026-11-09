# Java 8 - Supply Chain Inventory Deduplication

## Çfarë kërkohej?

Të gjejmë produkte që mund të jenë të njëjta, edhe kur furnitorët i shkruajnë
ndryshe. Produktet e reja duhet të krahasohen me inventarin ekzistues dhe me
njëri-tjetrin. Rezultati duhet të japë grupe për kontroll, nivelin e sigurisë
dhe produktet e reja që nuk kanë përputhje.

Përputhja përdor markën, modelin, madhësinë dhe ngjyrën. Madhësia dhe ngjyra
nxirren nga përshkrimi. Kërkohen tabela hash dhe një zgjidhje që shmang
krahasimin e çdo produkti me çdo produkt për 100,000+ regjistrime.

## Çfarë bëmë?

Ndërtuam një program Python 3.8+ pa paketa shtesë:

| Skedari | Puna e tij |
| --- | --- |
| `normalization.py` | Njëson shkrimin dhe nxjerr madhësitë e ngjyrat nga përshkrimi. |
| `deduplication.py` | Përdor tabela hash për grupimin dhe përcakton nivelin e sigurisë. |
| `main.py` | Lexon JSON, kontrollon hyrjen dhe shfaq raportin. |
| `example.json` | Përmban inventarin dhe produktet e reja nga shembulli i detyrës. |

Si dosjet e mëparshme, `java8` do të thotë java e tetë; kodi është Python.

## Si hapet?

Nga dosja kryesore e projektit:

```powershell
python java8/main.py
python java8/main.py java8/example.json --json
```

Ose nga brenda `java8`:

```powershell
python main.py
python main.py inventari_im.json
```

Pa rrugë hyrëse përdoret `example.json`. `--json` jep raport të strukturuar.
Programi shkruan në ekran dhe nuk ndryshon inventarin ose krijon skedarë.

## Hyrja

JSON ka dy lista: `inventory` dhe `incoming`. Secila mund të jetë bosh.
Çdo produkt duhet të ketë saktësisht pesë fusha tekst:

```json
{
  "product_id": "NEW001",
  "brand": "SAMSUNG",
  "model": "Galaxy S21",
  "description": "128 GB - Black Color",
  "supplier_id": "SUP-C"
}
```

`product_id` duhet të jetë unik në të dyja listat. ID-të e produktit dhe
furnitorit nuk mund të jenë bosh dhe dallojnë shkronjat e mëdha nga të voglat.
Marka, modeli dhe përshkrimi mund të jenë vargje bosh kur të dhënat mungojnë.
Fushat që mungojnë, fushat shtesë, llojet e gabuara, ID-të e përsëritura,
JSON i pavlefshëm ose skedari i palexueshëm japin mesazh gabimi dhe kod daljeje 1.
Përputhjet mund të jenë edhe brenda të njëjtit furnitor.

## Si njësohen të dhënat?

- Marka dhe modeli kalojnë në shkronja të vogla. Hiqen hapësirat,
  pikësimi dhe shenjat e theksimit kur ndahen nga Unicode. Kështu
  `SAMSUNG` përputhet me `Samsung`, ndërsa `WH-1000XM4` me `WH1000XM4`.
- `iPhone 13` dhe `iPhone 13 Pro` mbeten modele të ndryshme.
- Madhësia dhe ngjyra nxirren nga përshkrimi. Rendi i fjalëve nuk ndikon.
- Njihen MB/GB/TB, gigabyte/terabyte; mm/cm/in/inch/inches dhe shenja e
  inçit; ml/l/liter/litre dhe g/kg. Njësitë e të njëjtit lloj kthehen në një
  njësi të përbashkët: p.sh. `128GB` dhe `128 GB` bëhen `storage_mb:128000`.
  Ruajtja përdor njësitë dhjetore: 1 TB = 1000 GB. Një inç është 25.4 mm.
- Njihen madhësitë e rrobave XXS deri XXXL, 2XL/3XL, small/medium/large dhe
  etiketa numerike si `size 42`. Numra të tjerë si `4K` nuk merren si madhësi.
- Njihen ngjyrat dhe shkurtesat e zakonshme: black/blk/bk, white/wht/wh,
  blue/blu/bl, gray/grey/gry, green/grn, gold/gld, silver/slv dhe të tjera.
  Lista e plotë është te `COLOR_ALIASES`.
- Hapësirat, vizat mes numrit dhe njësisë, presjet ose pikat dhjetore dhe
  zerot në fund të pjesës dhjetore njësohen.
- Kur ka disa madhësi ose ngjyra, ruhen të gjitha pa përsëritje, në rend të
  qëndrueshëm. Black/white është ndryshe nga black i vetëm.
- Kur nuk nxirret asnjë vlerë, përdoret një tuple bosh `()`.
  Të dhënat origjinale ruhen në raport për kontroll nga përdoruesi.

## Si përdoret tabela hash?

1. Çdo produkt normalizohet një herë.
2. Çelësi është `(brand, model, sizes, colors)`. Një dictionary ruan të gjitha
   produktet me të njëjtin çelës në një grup.
3. Nëse grupi ka të paktën dy produkte dhe të paktën një është i ri,
   shfaqet një herë si grup HIGH. Nuk krijohen vetëm çifte: grupi mund të
   ketë shumë furnitorë dhe shumë produkte.
4. Për përputhjet me të dhëna që mungojnë përdoren katër forma të indeksit
   për çdo çelës. `None` është shenjë kërkimi për çdo vlerë, ndërsa `()` do të
   thotë që atributi mungon. Kështu nuk kontrollojmë të gjithë inventarin
   për çdo produkt të ri.
5. Produktet e reja që nuk morën pjesë në asnjë grup dalin si unike,
   në rendin fillestar.

Grupet që përmbajnë vetëm produkte të vjetra nuk shfaqen në këtë raport të
hyrjeve të reja. Përplasjet e hash-it nuk barazojnë produkte të ndryshme:
dictionary kontrollon edhe barazinë e çelësave të plotë.

## Nivelet e sigurisë

| Niveli | Rregulli | Pse? |
| --- | --- | --- |
| HIGH | Marka, modeli, madhësitë dhe ngjyrat përputhen pas normalizimit. Mungesa e një atributi te të dyja anët llogaritet si përputhje. | Ky është rregulli i kërkuar nga detyra. |
| MEDIUM | Marka dhe modeli janë jo bosh dhe njësoj. Një nga madhësia/ngjyra mungon vetëm te njëra anë; atributi tjetër përputhet. | Ka përputhje, por një pjesë e të dhënave nuk konfirmohet. |
| LOW | Marka dhe modeli janë jo bosh dhe njësoj. Si krahasimi i madhësisë, ashtu edhe ai i ngjyrës kanë vlerë që mungon vetëm te njëra anë. Nuk ka kundërshtim të njohur. | Kemi më pak informacion për të konfirmuar produktin. |
| Pa përputhje | Marka/modeli ndryshojnë, ose dy madhësi/ngjyra të njohura ndryshojnë. | Nuk bashkojmë variante që dihet se janë të ndryshme. |

Këto janë kategori për kontroll njerëzor, jo përqindje statistikore.
Sipas rregullit HIGH, edhe dy marka ose modele bosh numërohen si të barabarta.

Grupet MEDIUM/LOW janë propozime të veçanta dhe mund të mbivendosen me grupe
të tjera. Nuk bëjmë bashkim zinxhir: një produkt pa ngjyrë mund të propozohet
me një grup të zi dhe veçmas me një të bardhë, por i ziu dhe i bardhi nuk
futen së bashku. Çdo propozim përmban të gjithë anëtarët e dy grupeve të
sakta që krahasohen. Një grup HIGH mund të shfaqet edhe brenda një propozimi
me nivel më të ulët.

## Rezultati i pritshëm i shembullit

Ky është rezultati i pritshëm nga inspektimi i kodit, jo rezultat i ekzekutuar:

```text
DUPLICATE GROUPS FOUND:
Group 1 (Samsung Galaxy S21):
-PROD001 (Supplier: SUP-A)
-NEW001 (Supplier: SUP-C)
Confidence: HIGH

Group 2 (Sony WH-1000XM4):
-PROD003 (Supplier: SUP-B)
-NEW003 (Supplier: SUP-C)
Confidence: HIGH

Group 3 (Apple iPhone 13 Pro):
-NEW002 (Supplier: SUP-D)
-NEW005 (Supplier: SUP-E)
Confidence: HIGH

NEW UNIQUE PRODUCTS:
-NEW004 (LG OLED TV 55)
```

Samsung përputhet pavarësisht shkrimit të GB dhe markës. Sony përputhet
pavarësisht vizës në model. Dy produktet e reja Apple Pro përputhen mes tyre,
edhe pa një produkt të tillë në inventar. Apple iPhone 13 i vjetër nuk
përputhet me Pro sepse modeli ndryshon.

## Funksionet kryesore

| Funksioni | Çfarë bën dhe pse? |
| --- | --- |
| `normalized_text(value)` | Njëson markën/modelin që ndryshimet e shkrimit të mos pengojnë përputhjen. |
| `AttributeNormalizer.__init__()` | Përgatit rregullat e nxjerrjes një herë, që të ripërdoren për produktet. |
| `AttributeNormalizer.__call__(product)` | Nxjerr atributet dhe krijon një çelës të pandryshueshëm për hash-in. |
| `Product.__post_init__()` | Kontrollon fushat tekst dhe ID-të që produkti të ketë të dhëna të vlefshme. |
| `InventoryDeduplicator.__init__(normalize)` | Merr normalizuesin si varësi, që rregullat e nxjerrjes të zëvendësohen pa ndryshuar grupimin. |
| `find_duplicates(inventory, incoming)` | Ndërton indekset hash, krijon grupet dhe nxjerr produktet e reja pa përputhje. |
| `load_products(path)` | Lexon JSON dhe kontrollon formatin para se të nisë grupimi. |
| `print_report(result)` | Shfaq raportin tekst duke mbajtur paraqitjen jashtë logjikës së grupimit. |
| `main()` | Lidh hyrjen, algoritmin dhe daljen sipas argumenteve të komandës. |

## Shkallëzimi dhe kufizimet

Le të jenë N numri i produkteve, U numri i çelësave të ndryshëm, T gjatësia
totale e tekstit, C numri i çifteve të çelësave të përshtatshëm që vizitohen
dhe R numri i referencave të produkteve në raport. Koha e pritshme është
O(T + N + C + R), për kërkime hash mesatarisht konstante dhe atribute me
gjatësi të kufizuar. Renditja e bashkësive të atributeve shton koston e saj
lokale. Kujtesa është O(N + U + C + R), përfshirë raportin.

100,000 produkte me të njëjtin çelës krijojnë një grup, pa listuar çdo çift.
Indeksi ka maksimumi katër hyrje për çelës. Megjithatë, shumë produkte me të
dhëna të paplota mund të japin numër kuadratik propozimesh të vlefshme;
shfaqja e tyre kërkon kohë dhe kujtesë sipas madhësisë së rezultatit.
Programi lexon JSON dhe mban raportin në kujtesë; nuk është zgjidhje streaming
ose bazë të dhënash në disk. Nuk u krye matje me 100,000 produkte.

Fjalori i njohur i madhësive dhe ngjyrave është i kufizuar. Termat e panjohur
trajtohen si të dhëna që mungojnë dhe mund të shkaktojnë propozime të gabuara,
sidomos nën rregullin HIGH. Tekstet me mohim, aksesorët, përmasat me disa
dimensione, gabimet drejtshkrimore, sistemet rajonale të madhësive dhe emrat
alternativë të markave kërkojnë rregulla më të avancuara. Heqja e pikësimit
mund të bashkojë emra modelesh ku pikësimi ka kuptim. Programi vetëm propozon
kontroll; nuk bashkon ose ndryshon automatikisht produkte.

Teste nuk u shkruan ose ekzekutuan gjatë rikrijimit. Python nuk është i
disponueshëm në këtë shell, prandaj ekzekutimi dhe kontrolli sintaksor me
interpretues mbeten të pakonfirmuar.
