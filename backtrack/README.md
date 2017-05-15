# Futócsere probléma viszalépéses megoldáskeresői

A az alap viszalépéses megoldáskereső rendszerek az operátor választásának módjában térnek el.

## Figyelési módok

- Körfigyeléssel
- Úthosszkorláttal

## Operátor választásának módjai

### Első operátor

Kiválasztja az alkalmazható operátorok közül a legelsőt.
Körfigyeléssel hosszadalmas, de az állapottérgráf szerkezetéből adódóan előállít egy megoldást.
Megfelelő úthosszkorláttal szintén előállít egy megoldást.

### Véletlenszerű

Véges sok lépésben előállít egy megoldást (körfigyeléssel vagy megfelelő úthosszkorláttal)

### Heurisztikusan

Heurisztkia: Mennyire nincsenek a báúk a helyükön? ( Egy világos az első sorban: 4 | 5. sorban: 0 )
Körfigyeléssel vagy megfelelő úthosszkorláttal véges sok lépésben előállít egy megoldást.