def carica_da_file(file_path):
    from operator import itemgetter                         # importo itemgetter per ordinare il dizionario per sezione
    try:
        infile = open("file_path", 'r')                     # apro il file, il cui nome è passo come argomento dal main()
        dizionario=dict()                                   # creo un dizionario vuoto
        cont=0                                              # uso un contatore per gestire la prima riga dove con numero di sezioni,
        for line in infile:                                 # dalla seconda l'elenco di libri
            if cont==0:
                linea_pulita = line.strip("\n")             # leggo prima riga e la pulisco
                numero_sezioni=int( linea_pulita )
                print(f"numero_sezioni:",numero_sezioni)
                cont = 1
            else:
                linea_pulita = line.strip("\n").split( "," ) # prendo gli elementi li pulisco e li sistemo nel dizionario
                dizionario['titolo',linea_pulita[0]] ={'autore':linea_pulita[1],'anno':linea_pulita[2],'sezioni':linea_pulita[3]}
        dizionario=sorted(dizionario.items(), key=itemgetter(3))
        print(dizionario)                                    # stampo il dizionario per verifica
        infile.close()
        return dizionario                                    # se l'operazione di apertura va a buon fine restituisco il dizionario
    except FileNotFoundError:
        return None                                          # se l'apertura fallisce restituisco none come richiesto dal testo


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    infile=open("file_path", 'a')
    libro=input("inserire il nome del libro")
    if libro in biblioteca:
    lista=input("inserire il nome del libro")
    lista=infile.write(libro)

    """Aggiunge un libro nella biblioteca"""
    # TODO'''


def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        #stampo menù opzioni
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()


        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)  #file_path
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")

'''
if __name__ == "__main__":
    main()

