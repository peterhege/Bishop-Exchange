# Futócsere probléma nemmódosítható megoldáskeresői

A megoldáskereső rendszerek az operátor választásának módjában térnek el.

## Operátor választásának módjai

### Billentyűzetről

Az alkalmazható operátorok közül választhatunk.
1. Futó választás
2. Új pozíció választás

##### Teljesség

Véges sok lépésben megtalálható egy célállapot. A keresés semmilyen esetben sem sikertelen, mivel mindig van lehetőség a visszalépésre.

##### Optimalitás és Időigény

Felhasználótól függ.

### Véletlenszerű

Az algoritmus a választható operátorok közül véletlenszerűen választ egyet, majd alkalmazza.

##### Teljesség

A keresés semmilyen esetben sem sikertelen, mivel mindig van lehetőség a visszalépésre, így
- Véges sok lépésben megtalál egy célállapotot
- A végtelenségig fut ( tesztelés során még nem fordult elő )

##### Időigény

A véletlen választás miatt változó

### Hegymászó módszer

##### Heurisztika

- Minden futó cél sorától vett távolságának összege.
- Minden futóra nézve a következők összege: ha a kezdő pozícióban van: 2, ha nincs a helyén: 1, ha a helyén van: 0.
- Ezek összege

##### Teljesség

Sajnos mindhárom heurisztika esetén a keresés sikertelen, mert megáll egy olyan állapotban, ahol már nincs több alkalmazható operátor.
Egy operátor alkalmazásának heurisztikája nagyobb, mint az állapot heurisztikája, minden operátorra, melyek teljesítik az alkalmazási előfeltételeket.

##### Időigény

Pontos heurisztikával csökkenthető

## Tárigény

Mindhárom választás eseté a tárigény kicsi a Nemódosítható megoldáskereső rendszer algoritmusából adódóan.