import csv
import random

from Classe_Fascia import Fascia
from Classe_Programma import Prog


def popola_programmi(path_file):
    lista_programmi = []
    with open(path_file, newline='') as csvfile:
        cvs_file = csv.reader(csvfile, delimiter=';')
        prima_riga = True
        for riga in cvs_file:
            if prima_riga:
                prima_riga = False
            else:
                temp_prog = Prog(riga[0], int(riga[1]), int(riga[2]), riga[3])
                # print(f"Nome programma: {temp_prog.nome} repliche: {temp_prog.repliche}")
                for i in range(temp_prog.repliche):
                    lista_programmi.append(temp_prog)

    return lista_programmi


def popola_fasce(path_file):
    lista_fascie = []
    with open(path_file, newline='') as csvfile:
        cvs_file = csv.reader(csvfile, delimiter=';')
        prima_riga = True
        for riga in cvs_file:
            if prima_riga:
                prima_riga = False
            else:
                temp_fasc = Fascia(riga[0], int(riga[1]), riga[2])
                # print(f"Nome fascia: {temp_fasc.nome} Slot disponibili: {temp_fasc.num_slot}")
                for i in range(6):
                    lista_fascie.append(temp_fasc)

    return lista_fascie


def trova_giorno(numero):
    if numero / 3 < 1:
        return "Lunedi"
    elif numero / 3 < 2:
        return "Martedi"
    elif numero / 3 < 3:
        return "Mercoledi"
    elif numero / 3 < 4:
        return "Giovedi"
    elif numero / 3 < 5:
        return "Venerdi"
    elif numero / 3 < 6:
        return "Sabato"


def trova_fascia(numero):
    if numero % 3 == 0:
        return "Mattina"
    elif numero % 3 == 1:
        return "Pranzo"
    elif numero % 3 == 2:
        return "Cena"


def allocate_items(lista_fasce, lista_programmi):
    lista_programmi = sorted(lista_programmi, reverse=True)

    palinsesto = [[] for _ in range(len(lista_fasce))]

    for programma in lista_programmi:
        controllo = True
        while controllo:

            rand_val = random.randint(0, len(lista_fasce) - 1)

            rand_fascia = lista_fasce[rand_val]

            temp_slot_occup = sum([item.slot for item in palinsesto[rand_val]])

            # Controlla se ci solo slot disponibili
            if temp_slot_occup + programma.slot <= rand_fascia.num_slot:
                palinsesto[rand_val].append(programma)
                controllo = False

    return palinsesto


def controllo_doppioni(palinsesto):
    for allocation in palinsesto:
        if len(allocation) != len(set(allocation)):
            return False

    return True


def main():
    lista_fasce = popola_fasce("csv_files\Fasce.csv")

    tot_slot_dsp = 0
    for fascia in lista_fasce:
        tot_slot_dsp = tot_slot_dsp + fascia.num_slot

    lista_programmi = popola_programmi("csv_files\Programmi.csv")

    tot_slot_ric = 0
    for programma in lista_programmi:
        tot_slot_ric = tot_slot_ric + programma.slot

    print(f"Slot totali richiesti = {tot_slot_ric} / Slot totali disponibili = {tot_slot_dsp}")

    controllo = True

    while controllo:
        palinsesto = allocate_items(lista_fasce, lista_programmi)
        controllo = controllo_doppioni(palinsesto)

    for i, allocation in enumerate(palinsesto):
        print(f"Fascia {trova_fascia(i)} del {trova_giorno(i)}: {[programma.nome for programma in allocation]}")


if __name__ == '__main__':
    main()
