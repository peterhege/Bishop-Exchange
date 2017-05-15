# Futócsere probléma

## Probléma

Adott egy 5×4-es sakktábla, melynek alsó sorában sötét futók, felső sorában világos futók állnak úgy, ahogy
az ábrán látható.

![bishop table](bishop.jpg "Bishop table")

[Szabályos sakklépésekkel](https://en.wikipedia.org/wiki/Bishop_(chess)#Movement) cseréljük fel a világos futókat a sötétekkel.

Forrás: [Kósa Márk - Feladatgyűjtemény a Mesterséges intelligencia 1 című tantárgyhoz](https://arato.inf.unideb.hu/kosa.mark/mestint/feladatsor.pdf) 3.o / 4. feladat

## Állapottér reprezentáció

Részletesen: [bishop-exchange.pdf](docs/bishop-exchange.pdf)

## Megoldáskereső rendszerek

### Nem módosítható kereső

Részletesebben: [Itt](brute_force/)

Operátor választás módja:

- Billentyűzetről
- Véletlenszerűen
- Hegymászó módszerrel

### Visszalépéses kereső

Részletesebben: [Itt](backtrack/)

Operátor választás módja:

- Első választható operátor
- Véletlenszerűen
- Heurisztikus

Módok:

- Körfigyeléssel
- Úthosszkorláttal

### Szélességi és Mélységi kereső

Részletesebben: [Itt](depth/)

### Optimális kereső

Részletesebben: [Itt](optimal/)

### Best-First

Részletesebben: [Itt](best_first/)

### A algoritmus

Részletesebben: [Itt](a_algorithm/)