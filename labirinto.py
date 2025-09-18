def stampa_griglia(n, pos, uscita):
    """Stampa la griglia con P = giocatore, U = uscita, . = spazio vuoto"""
    # TODO


def muovi(pos, mossa):
    """Aggiorna la posizione in base alla mossa"""
    # TODO


def gestisci_livello(livello):
    """ Gestisce un singolo livello del labirinto
    La funzione deve ritornare un bool:
    * True se il giocatore raggiunge l'uscita
    * False se il giocatore va oltre i limiti della griglia.
    """

    # Inizializzazioni
    n = livello + 2
    pos = [0, 0]  # posizione iniziale
    uscita = [n - 1, n - 1]  # posizione uscita

    # TODO


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
