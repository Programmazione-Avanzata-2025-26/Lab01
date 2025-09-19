def stampa_griglia(n, pos, uscita):
    """Stampa la griglia con P = giocatore, U = uscita, . = spazio vuoto"""
    # TODO


def muovi(pos, mossa):
    """Aggiorna la posizione in base alla mossa"""
    if mossa == "n":
        pos[0] -= 1
    elif mossa == "s":
        pos[0] += 1
    elif mossa == "e":
        pos[1] += 1
    elif mossa == "o":
        pos[1] -= 1


def gestisci_livello(livello):
    """ Gestisce un singolo livello del gioco.
    Ritorna:
    * True se il giocatore raggiunge l'uscita
    * False se il giocatore va oltre i limiti della griglia.
    """

    # Inizializzazioni
    n = livello + 2
    pos = [0, 0]  # posizione iniziale
    uscita = [n - 1, n - 1]  # posizione uscita

    print(f"\nLivello {livello}) Griglia {n}x{n}")
    stampa_griglia(n, pos, uscita)

    while pos != uscita:
        mossa = input("Mossa (n/s/e/o): ").strip().lower()
        muovi(pos, mossa)

        # controllo uscita dai limiti
        if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= n:
            print("GAMEOVER: Sei uscito dalla griglia!")
            return False

        stampa_griglia(n, pos, uscita)

    print("Hai raggiunto l’uscita!")
    return True


def main():
    print("=== Benvenuto al Gioco del Labirinto ===")
    livello = 0
    max_livello = 5

    while livello <= max_livello:
        completato = gestisci_livello(livello)
        if completato:
            livello += 1
        else:
            break


if __name__ == "__main__":
    main()
