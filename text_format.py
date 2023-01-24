"""
Dato un determinato quantitativo di testo, viene suddiviso in blocchi per  tipo di informazioni,
ogni blocco equivale ad un paragrafo, 
al loro interno vengono suddivisi ulteriormente in righe: ogni ~ 70 (o poco più) caratteri \\n;

I blocchi a loro volta vengono numerati partendo da 1, vengono disposti in 2 colonne (1 e 2),
dove gli indici pari indicano i blocchi che stanno a sinistra, i dispari a destra,
i blocchi vengono divisi tra di loro da 2 righe vuote,
i blocchi vengono contati in valori assoluti, non blocchi per colonna;

Quando viene cercata una determinata parola si otterrà il seguente risultato:
\"parola non presente\" se non viene trovata in alcun blocco, altrimenti,
\"parola trovata in B:[n blocco/chi] , C:[n colonna/e], R:[n riga]\"
"""

def spiegazione_file():
    """Printa la spiegazione di come viene ordinato il testo e come venga diviso in righe"""
    print(__doc__)


def scrittura_blocchi(lista_righe_blocco):
    """Scrive un blocco di testo in più righe"""
    with open('file.txt','a') as f:
        f.write('\n\n')
        for riga in lista_righe_blocco:
            f.write(riga + '\n')
        

def ordina_in_righe(testo):
    """Funzione che divide un testo di lunghezza indefinita riga di circa 70 caratteri."""
    # Setto delle variabili temporanee per i caratteri estremi di una parola
    if len(testo) <= 70:
        return testo

    else:

        lista_righe = []
        testo_da_ordinare = testo[:]

        # Controlla se il testo da analizzare sia di lunghezza maggiore di 70 caratteri
        while len(testo_da_ordinare) > 70:
            end_line_char = 70

            # Se il 70esimo carattere è uno spazio o un punto, o una virgola il testo va a capo e viene aggiunto come riga
            if testo_da_ordinare[70] in [' ', '.', ',']:
                lista_righe.append(testo_da_ordinare[:71])
                testo_da_ordinare = testo_da_ordinare[71:]

            # Se il 70esimo carattere è una lettera continuo a cercare finchè non trovo un carattere che permetta di andare a capo
            else:
                
                while testo_da_ordinare[end_line_char] not in [' ', '.', ',']:
                    end_line_char += 1
                
                lista_righe.append(testo_da_ordinare[:end_line_char+1])
                testo_da_ordinare = testo_da_ordinare[end_line_char+1:]

        # Se la lunghezza del testo da analizzare è minore di 70 caratteri aggiunge il testo come riga singola
        else:
                lista_righe.append(testo_da_ordinare)
        
        return lista_righe


blocco1 = "Sed elementum fringilla elementum. Nam non convallis erat. Donec venenatis nisl quis mi eleifend, in porttitor enim volutpat. Maecenas et sapien maximus, vulputate nisi sed, ultricies erat. Maecenas nec velit at lacus vulputate consectetur. Aenean non blandit nunc, et lobortis magna. Vestibulum tincidunt ultrices turpis, non faucibus mauris hendrerit at. Praesent malesuada ultricies neque, eget tincidunt massa aliquam quis. Phasellus rutrum quis ligula eu suscipit. Donec sodales ullamcorper orci quis aliquam."
blocco2 = "Proin eleifend, magna quis vestibulum aliquet, velit turpis faucibus leo, ac vehicula leo felis non dolor. Maecenas dapibus molestie turpis pharetra iaculis. Quisque ac mattis sem. Integer ipsum risus, faucibus nec elit id, dapibus viverra velit. Donec dictum auctor pharetra. Nulla varius sapien nec consequat iaculis. Suspendisse eget massa pharetra, imperdiet erat id, vehicula arcu. Aliquam auctor dapibus sem, in volutpat eros. Aliquam ultricies venenatis mattis. Curabitur justo erat, laoreet at posuere vitae, semper eget magna. Morbi iaculis luctus neque, vel volutpat elit cursus id. Nulla non eros ac nisi consectetur interdum et eu nibh. Aenean rhoncus, ipsum sit amet varius tempor, quam nulla vulputate lacus, et molestie dolor sem vitae libero. Curabitur cursus eros ut quam ultricies egestas. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Phasellus dictum mi turpis, eu dapibus velit interdum vel."
blocco3 = "Maecenas gravida at ex iaculis gravida. Duis cursus, libero eget rutrum consectetur, nibh mauris eleifend tortor, vel euismod massa quam nec risus. Vestibulum id lacus interdum, fringilla dolor ac, scelerisque risus. Nullam porta imperdiet semper. Pellentesque varius velit tortor, ac tristique arcu fringilla et. Praesent molestie pretium nibh, vel vulputate nisi euismod a. In finibus nibh libero, vel posuere elit condimentum in. Curabitur nulla ipsum, pellentesque sit amet nunc rutrum, finibus dapibus mauris."
blocco4 = "Quisque consequat imperdiet augue. Maecenas nisi mauris, interdum id erat nec, maximus cursus massa. Vivamus fringilla, nisl in pretium congue, massa orci tempus ante, vitae dignissim odio sem commodo orci. Donec sed lacus justo. Pellentesque faucibus, risus eu facilisis varius, tortor justo porttitor eros, quis interdum leo tortor non diam. Nullam consequat feugiat ante, in tincidunt erat viverra quis. Vestibulum ut mauris hendrerit, venenatis lorem dapibus, faucibus arcu. Sed vel elit ac felis pulvinar lacinia. Phasellus fermentum, nulla ac malesuada vulputate, nunc velit faucibus ligula, a consequat est urna non enim. Sed malesuada leo ligula, viverra condimentum turpis porta quis. Ut purus nisi, pharetra quis lorem eu, ultrices feugiat libero."
blocco5 = "Phasellus iaculis pharetra turpis, a pharetra ipsum. Pellentesque maximus mi eget libero consectetur, volutpat rutrum sapien vulputate. Proin mollis bibendum leo nec tincidunt. Proin molestie felis sed justo aliquam, quis volutpat tellus mattis. Vestibulum est mauris, tempor in pellentesque id, convallis ut ante. Donec sagittis urna a lacus tempor, quis bibendum neque ornare. Donec finibus lorem et ex semper, dictum volutpat felis maximus. Integer ligula dolor, pretium in justo nec, euismod mollis lacus. Integer quis augue ac libero varius pulvinar. Fusce vitae nibh et nisl tristique posuere."
blocco6 = "Phasellus id nunc finibus, condimentum tellus sollicitudin, vulputate odio. Cras diam mi, semper nec leo in, placerat cursus sapien. Nulla nec fringilla dui. Praesent a urna a velit vestibulum hendrerit. Etiam ut sem hendrerit arcu bibendum ornare. Aliquam finibus pharetra est eget dapibus. Fusce quis libero dignissim, viverra lacus in, lacinia augue. Vivamus consectetur, tellus facilisis venenatis venenatis, mauris ex posuere leo, nec dignissim justo elit id magna. Vivamus dapibus, sapien non accumsan sollicitudin, massa odio faucibus metus, et pulvinar nulla leo et magna. Donec hendrerit et nisi in interdum. Cras consequat orci nisl, quis luctus est pellentesque vitae. Etiam iaculis scelerisque odio convallis rutrum. Fusce suscipit lacinia orci nec aliquet. Integer interdum finibus dolor, in vehicula justo congue at. Cras cursus porttitor sagittis. In at ipsum ex."
blocco7 = "Nullam aliquam eros at faucibus bibendum. Praesent commodo nulla sit amet elementum lacinia. Proin elementum lectus et arcu efficitur rhoncus. Cras ut semper magna. Proin ligula est, dictum non sagittis blandit, ornare nec orci. Curabitur finibus erat eu turpis feugiat, vel ultricies nunc venenatis. Quisque euismod enim id tristique tincidunt. Nullam auctor, purus ut tristique porta, quam purus commodo purus, vel malesuada justo velit sit amet ligula. Etiam dolor libero, consequat in rhoncus ut, tristique non diam. Donec iaculis vestibulum purus, quis facilisis metus fermentum non. Vestibulum enim dui, pulvinar eu nisl nec, pulvinar consequat massa. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec efficitur in tellus nec euismod. Vivamus iaculis, metus sit amet maximus dapibus, felis erat ornare mi, quis posuere ipsum tellus id mauris. Nam ac lacinia nunc, sed accumsan augue."
blocco8 = "Proin pellentesque imperdiet arcu, ullamcorper molestie lectus maximus quis. Sed mauris nunc, pharetra nec sodales nec, condimentum nec elit. Integer a egestas magna. Ut quis massa non est sodales sodales. In a felis eget libero hendrerit suscipit quis in velit. Aliquam quis mattis enim. Quisque rhoncus dolor et maximus fringilla. Suspendisse id magna sed mauris congue facilisis. Pellentesque aliquet vel ligula vitae efficitur. Praesent eget sem eget ligula congue egestas. Proin molestie, arcu ac molestie tempus, ipsum metus congue tortor, et hendrerit dolor nibh id nisi. Cras eget velit hendrerit, iaculis eros vitae, dapibus elit. In interdum erat nec vulputate interdum. Aenean quis urna in nisi lacinia accumsan quis at ipsum. Donec fringilla ullamcorper ligula eu mollis. Maecenas semper iaculis justo, at malesuada tortor."
blocco9 = "Vivamus euismod quis ipsum in ornare. Praesent lacinia arcu vitae urna consectetur convallis. Nam varius tellus a ex accumsan, a sagittis urna varius. Sed orci neque, ullamcorper sit amet semper vitae, tincidunt interdum quam. Aliquam non quam sed mi iaculis placerat. Nullam eget risus lorem. Mauris quis est venenatis, sodales orci laoreet, rutrum mi. Cras elementum leo porta, egestas diam lobortis, feugiat ipsum. Duis feugiat ex velit, vel dignissim purus tempus at. Cras porta elit dui, quis pretium metus varius fermentum. Ut vel urna feugiat, convallis ante at, consectetur turpis. Etiam consequat, ante ut mollis dapibus, diam dolor molestie arcu, a porttitor nisi diam in risus. Nulla ultricies urna eget turpis accumsan tempus."
blocco10 = "Fusce in mi ac nibh cursus interdum. Mauris eleifend ultrices lobortis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam nulla mi, consectetur sollicitudin lectus quis, blandit iaculis neque. Proin nisl mauris, luctus at risus vitae, tristique porttitor orci. Etiam tristique viverra euismod. In id mollis magna. In sit amet congue ante."

lista_blocchi = [blocco1, blocco2, blocco3, blocco4, blocco5, blocco6, blocco7, blocco8, blocco9, blocco10]


# for blocco in lista_blocchi:
#     scrittura_blocchi(ordina_in_righe(blocco))