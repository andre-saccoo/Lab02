def carica_da_file(file_path):
    # importo itemgetter per ordinare il dizionario per sezione
    from operator import itemgetter
    try:
        # apro il file, il cui nome è passo come argomento dal main() e creo un dizionario vuoto che vado poi a riempire con i libri
        infile = open(file_path, 'r', encoding='utf-8')
        biblioteca=dict()
        # uso un contatore per gestire la prima riga contenente il numero di sezioni, dalla seconda l'elenco di libri
        cont=0
        for line in infile:
            if cont==0:
                linea_pulita = line.strip("\n")
                numero_sezioni=int( linea_pulita )
                print(f"numero_sezioni:",numero_sezioni)
                cont = 1
            else:
                # prendo gli elementi li pulisco e li sistemo nel dizionario
                linea_pulita = line.strip("\n").split( "," )
                biblioteca[linea_pulita[0]] =[linea_pulita[1],linea_pulita[2],linea_pulita[3],linea_pulita[4]]
        infile.close()

        biblioteca = {k: v for k, v in sorted(biblioteca.items(), key=itemgetter(3))}

        # stampo il dizionario per verifica per mostrarlo all'utente
        for titolo, info in biblioteca.items():
            print(f"titolo: {titolo}  informazioni: {info}")

        # se l'operazione di apertura va a buon fine restituisco il dizionario
        return biblioteca
    except FileNotFoundError:
        # se l'apertura fallisce restituisco none come richiesto dal testo
        return None

def aggiungi_libro(biblioteca, file_path):
    # controllo se file file_path è già stato aperto sopra
    if not biblioteca:
        print("Prima carica la biblioteca da file.")
        return None,biblioteca

    # chiedo il nome del libro che si vuole aggiungere
    titolo = input("Titolo del libro: ").strip()
    # controllo se il libro è già presente nella libreria, lancio la funzione
    if titolo in biblioteca:
        return None, biblioteca

    else:
        # se il libro non è presente controllo i campi conversione e li gestisco con le eccezioni
        autore = input("Autore: ").strip()
        try:
            anno = int(input("Anno di pubblicazione: ").strip())
            pagine = int(input("Numero di pagine: ").strip())
            sezione = int(input("Sezione: ").strip())
        except ValueError:
            print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
            return None, biblioteca

        biblioteca[titolo]={autore, anno, pagine, sezione}
        infile = open(file_path, 'a')
        infile.write(f'{titolo},{anno},{pagine},{sezione}\n')
        infile.close()
        return True, biblioteca


def cerca_libro(biblioteca, titolo):
    lista_chiavi=[]
    for chiave in biblioteca:
        lista_chiavi.append(chiave.lower())
    if titolo.lower() in lista_chiavi:
        return True
    else:
        return False

def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    for libro, info in biblioteca.items():
        if int(info[3])==sezione:
            print(libro)

def main():
    biblioteca = dict()
    file_path = "biblioteca.csv"

    while True:
        # stampo menù opzioni
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")
        scelta = input("Scegli un'opzione >> ").strip()

       #scelta 1 creo la struttura dati caricando dal file indicato l'elenco dei libri
        if scelta == "1":
            while True:
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break


        # scelta 2 aggiungo alla struttura dati il libro richiesto controllando non sia già presente, lo aggiungo anche al file
        elif scelta == "2":
            aggiunto=False
            aggiunto, biblioteca=aggiungi_libro( biblioteca, file_path)
            #se riesco ad aggiungere il libro la funzione restituisce true, se non viene aggiunto None come richiesto
            if aggiunto:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro")


        elif scelta == "3":
            #comtrollo la libreria non sia vuota
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            #inserisco il titolo da cercare e lo passo alla funzione cerca libro dopo averlo pulito, restituisce True o None
            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato!")
            else:
                print("Libro non trovato.")



        elif scelta == "4":
            #comtrollo la libreria non sia vuota
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione: ").strip())
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

if __name__ == "__main__":
    main()

