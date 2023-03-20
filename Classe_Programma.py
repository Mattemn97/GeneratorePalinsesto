# Classe che rappresente il programma da inserire in palinsesto


class Prog:
    def __init__(self, nome, durata, repliche, conduttori):
        self.nome = nome
        self.durata = durata
        self.conduttori = conduttori
        self.repliche = repliche

        # Il numero di slot è calcolato tenendo conto di uno slot minimo di 30 minuti
        slot = int(durata / 30)
        self.slot = slot

    def __sizeof__(self) -> int:
        return self.slot

    def __lt__(self, other):
        return self.slot < other.slot
