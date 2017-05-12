# Nemmódosítható megoldáskereső rendszerek

## Operátor választásának módjai

### Billentyűzetről

Az alkalmazható operátorok közül választhatunk.
1. Futó választás
2. Új pozíció választás

Mivel mindig van lehetőségünk visszalépni, ezért a keresés nem lesz sikertelen.

### Véletlenszerű

Az algoritmus a választható operátorok közül véletlenszerűen választ egyet, majd alkalmazza.

Mivel mindig van lehetőségünk visszalépni, ezért véges sok lépésben megtalál egy célállapotot.

### Hegymászó módszer

##### Heurisztika

Minden futó cél sorától vett távolságának összege.

Sajnos ez a keresés sikertelen, mert megáll egy olyan állapotban, ahol minden operátor - melyek teljesítik az alkalmazási előfeltételeket - alkalmazásának heurisztikája nagyobb, mint az állapot heurisztikája, melyben megáll az algoritmus.