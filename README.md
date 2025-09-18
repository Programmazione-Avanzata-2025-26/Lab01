# Lab 01

#### Obiettivi

- Ripasso e consolidamento dei concetti base: strutture condizionali e cicli
- Strutture dati base: variabili, array, liste
- Approccio modulare alla scrittura del codice (funzioni)
- Gestione interattiva di input utente.

## Gioco del Labirinto
Si vuole realizzare un programma in Python per gestire un gioco in cui il giocatore deve raggiungere l’uscita di un labirinto rappresentato da una griglia.

---

## Griglia e livelli

Ogni livello del gioco è una griglia quadrata di dimensione crescente:  

- **Livello 0** → griglia 2x2  
- **Livello 1** → griglia 3x3  
- **Livello 2** → griglia 4x4  
- … fino al livello massimo definito nel programma (es. livello 5)

Il giocatore parte sempre dalla cella in alto a sinistra `[0,0]` e l’uscita è sempre in basso a destra `[n-1,n-1]`.

### Simboli nella griglia

- `P` → giocatore  
- `U` → uscita  
- `.` → spazio vuoto

### Esempio di griglia livello 2 (4x4)

```console
P . . .
. . . .
. . . .
. . . U
```

---

## Regole del gioco

1. Il gioco inizia al livello 0.  
2. Il giocatore inserisce una mossa:  
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

Il sample fornito `labirinto.py` contiene già la funzione `main()` e le definizioni delle funzioni principali che dovrete implementare:

---

### `gestisci_livello(livello)`

**Descrizione:** Gestisce un singolo livello del labirinto, mostrando la griglia e gestendo i movimenti.

**Parametri:**
- `livello` (int): numero del livello corrente (determina la dimensione della griglia)

**Valore di ritorno:**
- `True` se il giocatore raggiunge l’uscita
- `False` se il giocatore esce dai limiti della griglia

---

### `stampa_griglia(n, pos, uscita)`

**Descrizione:** Stampa la griglia con il giocatore, l’uscita e gli spazi vuoti.

**Parametri:**
- `n` (int): dimensione della griglia (n x n)
- `pos` (list of int): posizione corrente del giocatore `[riga, colonna]`
- `uscita` (list of int): posizione dell’uscita `[riga, colonna]`

**Output:** Stampa a video la griglia. Nessun valore di ritorno.

---

### `muovi(pos, mossa)`

**Descrizione:** Aggiorna la posizione del giocatore in base alla mossa inserita.

**Parametri:**
- `pos` (list of int): posizione corrente del giocatore `[riga, colonna]`
- `mossa` (str): direzione della mossa (`n`, `s`, `e`, `o`)

**Output:** Aggiorna `pos` in-place. Nessun valore di ritorno.

---

## Esempio di esecuzione
```console
=== Benvenuto al Gioco del Labirinto ===

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
