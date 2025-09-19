# Lab 01

#### Obiettivi

- Ripasso e consolidamento dei concetti base: strutture condizionali e cicli
- Strutture dati base: variabili e liste
- Approccio modulare alla scrittura del codice (funzioni)
- Gestione interattiva di input utente.


## Gioco del Labirinto

Si vuole realizzare un programma in Python per gestire un gioco in cui il giocatore deve raggiungere l’uscita 
di una stanza rappresentata attraverso una griglia.

---

## Griglia e livelli

Ogni livello del gioco è una griglia quadrata di dimensione crescente:  

- **Livello 0** → griglia 2x2  
- **Livello 1** → griglia 3x3  
- **Livello 2** → griglia 4x4  
- … fino al livello massimo definito nel programma (es. livello 5)

Il giocatore parte da una posizione randomica `[x,y]` e l’uscita è sempre in basso a destra `[n-1,n-1]`.

**NB**: Per generare un numero randomico basta importare il modulo [`random`](https://docs.python.org/3.11/library/random.html) e usare le funzioni che mette a disposizione. 

### Simboli nella griglia

- `G` → giocatore  
- `U` → uscita  
- `.` → spazio vuoto

### Esempio di griglia livello 2 (4x4), giocatore in `[0,1]`

```console
. G . .
. . . .
. . . .
. . . U
```

---

## Regole del gioco

1. Il gioco inizia al livello 0.  
2. Il giocatore inserisce una mossa attraverso la tastiera:  
   - `n` → nord (su)  
   - `s` → sud (giù)  
   - `e` → est (destra)  
   - `o` → ovest (sinistra)  
3. La posizione del giocatore viene aggiornata sulla griglia.  
4. Il gioco termina in due casi:  
   - il giocatore esce dai limiti della griglia → **livello perso**  
   - il giocatore raggiunge l’uscita → **livello completato**    
5. Il gioco termina quando il giocatore perde oppure raggiunge il livello massimo completandolo.

---

## Funzioni da implementare

Il programma di base fornito `room_escape.py` contiene già le definizioni delle funzioni principali che dobranno essere implementate:

---

### `gestisci_livello(livello)`

**Descrizione:** Gestisce un singolo livello del labirinto, mostrando la griglia e aggiornando i movimenti.

**Parametri:**
- `livello`: un intero rappresentante il numero del livello corrente.

**Valore di ritorno:**
- `True` se il giocatore raggiunge l’uscita.
- `False` se il giocatore esce dai limiti della griglia.

---

### `stampa_griglia(n, pos, uscita)`

**Descrizione:** Stampa la griglia con il giocatore, l’uscita e gli spazi vuoti.

**Parametri:**
- `n`: un intero che indica la dimensione della griglia (n x n).
- `pos`: una lista di due interi con le coordinate `[riga, colonna]` della posizione corrente del giocatore.
- `uscita`: una lista di due interi con le coordinate `[riga, colonna]` della posizione dell’uscita.

**Output:** Stampa la griglia nella console. Nessun valore di ritorno.

---

### `muovi(pos, mossa)`

**Descrizione:** Aggiorna la posizione del giocatore in base alla mossa inserita.

**Parametri:**
- `pos`: una lista di due interi con le coordinate `[riga, colonna]` della posizione corrente del giocatore.
- `mossa`: una stringa contenente le possibili direzione della mossa (`n`, `s`, `e`, `o`).

**Output:** Aggiorna la posizione del giocatore (aggiornando la lista, eventualmente restituendo anche una lista aggiornata come valore di ritorno).

---

## Esempio di esecuzione
```console
=== Benvenuto in Room Escape ===

Livello 0) Griglia 2x2
P .
. U
Mossa (n/s/e/o): s
. .
P U
Hai raggiunto l’uscita!

Livello 1) Griglia 3x3
P . .
. . .
. . U
Mossa (n/s/e/o): s
. P .
. . .
. . U
Mossa (n/s/e/o): s
. . .
. P .
. . U
Mossa (n/s/e/o): e
. . .
. . P
. . U
Hai raggiunto l’uscita!

Livello 2) Griglia 4x4
P . . .
. . . .
. . . .
. . . U
Mossa (n/s/e/o): n
GAMEOVER: Sei uscito dalla griglia!

```
