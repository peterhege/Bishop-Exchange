# Futócsere probléma

## Probléma

Adott egy 5×4-es sakktábla, melynek alsó sorában sötét futók, felső sorában világos futók állnak úgy, ahogy
az ábrán látható.

![bishop table](bishop.jpg "Bishop table")

[Szabályos sakklépésekkel](https://en.wikipedia.org/wiki/Bishop_(chess)#Movement) cseréljük fel a világos futókat a sötétekkel.

Forrás: [Kósa Márk - Feladatgyűjtemény a Mesterséges intelligencia 1 című tantárgyhoz](https://arato.inf.unideb.hu/kosa.mark/mestint/feladatsor.pdf)

## Állapottér reprezentáció

Részletesen: [bishop-exchange.pdf](docs/bishop-exchange.pdf)

## Megoldáskereső rendszerek

### Nem módosítható kereső

Részletesebben: [brute-force](brute-force/)

Operátor választás módja:

- Billentyűzetről
- Véletlenszerűen
- Hegymászó módszerrel