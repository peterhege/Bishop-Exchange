# Futócsere probléma, Nemmódosítható megoldáskereső rendszerei

## Operátor választásának módjai

### Billentyűzetről

Az alkalmazható operátorok közül választhatunk.
1. Futó választás
2. Új pozíció választás

##### Teljesség

Véges sok lépésben megtalálható egy célállapot. A keresés semmilyen esetben sem sikertelen, mivel mindig van lehetőség a visszalépésre.

### Véletlenszerű

Az algoritmus a választható operátorok közül véletlenszerűen választ egyet, majd alkalmazza.

##### Teljesség

A keresés semmilyen esetben sem sikertelen, mivel mindig van lehetőség a visszalépésre, így
- Véges sok lépésben megtalál egy célállapotot
- A végtelenségig fut ( tesztelés során még nem fordult elő )

### Hegymászó módszer

##### Heurisztika

Minden futó cél sorától vett távolságának összege.

##### Teljesség

Sajnos ez a keresés sikertelen, mert megáll egy olyan állapotban, ahol már nincs több alkalmazható operátor.
Egy operátor alkalmazásának heurisztikája nagyobb, mint az állapot heurisztikája, minden operátorra, melyek teljesítik az alkalmazási előfeltételeket.