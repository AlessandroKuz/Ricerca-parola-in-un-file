from text_format import spiegazione_file


def cerca_parola(parola_da_cercare):
    """Restituisce il numero e la posizione delle occorrenze di una data parola all'interno di un testo"""
    # Aggiungo ogni occorrenza di una parola all'interno della lista richiamando la funzione ricerca
    lista_occorrenze = ricerca(parola_da_cercare)

    # Se parola presente almeno 1 volta restituire numero e posizione di ogni occorrenza
    if len(lista_occorrenze) > 0:

        print(f'Trovato "{parola_da_cercare}" {len(lista_occorrenze)} volte in posizione: ')
        # Stampo a schermo ogni occorrenza della parola interessata la posizione nella quale è stata individuata
        for indice, occorrenza in enumerate(lista_occorrenze):
            print(f"\t N.{indice+1}\tN.Blocco: {occorrenza[0]}\t N.Colonna: {occorrenza[1]}\t N.Riga: {occorrenza[2]}")
    
    # Se parola non presente restituire il messaggio corrispondente
    else:
        print(f'La parola "{parola_da_cercare}" non è presente nel testo!')


def ricerca(parola_da_cercare):
    """Cerca all'interno di un file di testo se è presente una parola, nel caso positivo restituisco una lista contenente la posizione di ogni occorrenza"""
    numero_blocco_corrente = 0
    contatore_righe_vuote = 0
    numero_riga_corrente = 0
    lista_posizioni = [] 

    with open("file.txt", "r") as f:
        for riga in f.readlines():
            # Se riga vuota aumento il contatore - fare in modo che siano due consecutive | in modo che non ci sia una riga in mezzo al testo
            if riga == '\n':
                contatore_righe_vuote += 1
                # Se due righe vuote di fila mi trovo davanti ad un nuovo blocco, aggiorno i dati di conseguenza
                if contatore_righe_vuote == 2:
                    numero_blocco_corrente += 1
                    contatore_righe_vuote = 0
                    numero_riga_corrente = 0
            # Se la riga contiene testo aggiorno il numero della riga corrente e controllo se la parola è presente in essa, se sì allora aggiorno la lista delle posizioni
            else:
                numero_riga_corrente += 1
                if parola_da_cercare in riga.lower():
                    numero_colonna_corrente = 1 if numero_blocco_corrente % 2 == 0 else 2
                    lista_posizioni.append((numero_blocco_corrente, numero_colonna_corrente, numero_riga_corrente))
        
    return lista_posizioni


# Per spiegazione su come verrà trattato e come viene formattato il file
# spiegazione_file()

# Presentazione dell'algoritmo di ricerca all'utente
print("""
Per ricercare un parola all'interno del testo digitare il termine ricercato e premere invio,
ripetere il processo per quante volte necessario, una volta finito digitare \"q\" e premere invio, ciò chiuderà il programma,
una volta inviato il termine da ricercare, verranno restituiti il/i [numero di blocco] [numero colonna] e [numero riga],
se si vuole una spiegazione di come viene organizzato il file di testo digitare \"spiegazione_testo\".
""")

# Definizione di 2 casi particolari nella ricerca del testo
caso1 = "spiegazione_testo"
caso2 = "visualizza_testo"

# Richiesta in input finche non viene chiuso il programma digitando "q"
parola_cercata = ""
while parola_cercata.lower() != "q":
    parola_cercata = input("Inserisci una parola da cercare all'interno del testo: ")

    # Converto la parola da cercare in minuscolo affinchè essa possa essere cercata e trovare pur se presenta o meno differenza di scrittura (maiuscole/minuscole)
    parola_cercata = parola_cercata.lower()

    # Se ci troviamo nel caso 1, stampa a schermo come viene organizzato il file passandoli x stringhe
    if parola_cercata == caso1:
        spiegazione_file()
        print("\nSe vuoi ulteriormente visualizzare tutto il testo puoi digitare \"visualizza_testo\"")
    
    # Se ci troviamo nel caso 1, stampa a schermo il testo del file
    if parola_cercata == caso2:
        with open("file.txt", "r") as f:
            print(f.read())
    
    # Se non siamo in nessuno dei 2 casi specifici allora bisogna controllare viene immessa solo una parola da ricercare, altrimenti divido in più parole e ne cerco una per volta
    if parola_cercata not in [caso1, caso2, "q"]:
        lista_parole_cercate = parola_cercata.split()
        if len(lista_parole_cercate) == 1:
            cerca_parola(lista_parole_cercate[0])
        
        else:
            for parola in lista_parole_cercate:
                cerca_parola(parola)
